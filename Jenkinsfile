pipeline {
    agent any

    environment {
        // Project info
        PROJECT_NAME = 'mindease-chatbot'

        // SonarQube (server name must match Jenkins > Configure System > SonarQube)
        SONAR_PROJECT_KEY = 'mindease-chatbot'

        // Render & Vercel deploy hooks (stored as Jenkins Secret Text credentials)
        RENDER_DEPLOY_HOOK  = credentials('render-deploy-hook')
        VERCEL_DEPLOY_HOOK  = credentials('vercel-deploy-hook')
    }

    options {
        // Keep last 5 builds
        buildDiscarder(logRotator(numToKeepStr: '5'))
        // Fail if pipeline takes longer than 30 min
        timeout(time: 30, unit: 'MINUTES')
        timestamps()
    }

    stages {

        // ─────────────────────────────────────────
        stage('Checkout') {
        // ─────────────────────────────────────────
            steps {
                echo "Checking out branch: ${env.BRANCH_NAME ?: 'main'}"
                checkout scm
            }
        }

        // ─────────────────────────────────────────
        stage('Install Dependencies') {
        // ─────────────────────────────────────────
            parallel {
                stage('Backend (pip)') {
                    steps {
                        echo 'Installing Python dependencies...'
                        sh 'pip install --quiet -r requirements.txt'
                    }
                }
                stage('Frontend (npm)') {
                    steps {
                        echo 'Installing Node dependencies...'
                        dir('frontend') {
                            sh 'npm ci --silent'
                        }
                    }
                }
            }
        }

        // ─────────────────────────────────────────
        stage('SonarQube Analysis') {
        // ─────────────────────────────────────────
            steps {
                echo 'Running SonarQube analysis...'
                withSonarQubeEnv('SonarQube') {
                    sh """
                        sonar-scanner \
                          -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                          -Dsonar.projectName='MindEase Mental Health Chatbot' \
                          -Dsonar.sources=api.py,src \
                          -Dsonar.exclusions=**/node_modules/**,data/**,models/**,reports/**,frontend/**,**/__pycache__/**,src/train_models.py,src/evaluate_models.py,src/roc_auc.py \
                          -Dsonar.python.version=3.11
                    """
                }
            }
        }

        // ─────────────────────────────────────────
        stage('Quality Gate') {
        // ─────────────────────────────────────────
            steps {
                echo 'Waiting for SonarQube Quality Gate result...'
                // Waits up to 5 minutes for quality gate result
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        // ─────────────────────────────────────────
        stage('Build Docker Images') {
        // ─────────────────────────────────────────
            parallel {
                stage('Build Backend Image') {
                    steps {
                        echo 'Building backend Docker image...'
                        sh "docker build -t ${PROJECT_NAME}-backend:${env.BUILD_NUMBER} -t ${PROJECT_NAME}-backend:latest ."
                    }
                }
                stage('Build Frontend Image') {
                    steps {
                        echo 'Building frontend Docker image...'
                        sh """
                            docker build \
                              --build-arg VITE_API_URL=http://localhost:8000 \
                              -t ${PROJECT_NAME}-frontend:${env.BUILD_NUMBER} \
                              -t ${PROJECT_NAME}-frontend:latest \
                              ./frontend
                        """
                    }
                }
            }
        }

        // ─────────────────────────────────────────
        stage('Deploy Backend → Render') {
        // ─────────────────────────────────────────
            steps {
                echo 'Triggering Render deploy for backend...'
                sh """
                    curl -s --fail -X POST "${RENDER_DEPLOY_HOOK}" \
                      -o /dev/null \
                      -w "HTTP Status: %{http_code}\\n"
                """
                echo 'Render deploy triggered successfully!'
            }
        }

        // ─────────────────────────────────────────
        stage('Deploy Frontend → Vercel') {
        // ─────────────────────────────────────────
            steps {
                echo 'Triggering Vercel deploy for frontend...'
                sh """
                    curl -s --fail -X POST "${VERCEL_DEPLOY_HOOK}" \
                      -o /dev/null \
                      -w "HTTP Status: %{http_code}\\n"
                """
                echo 'Vercel deploy triggered successfully!'
            }
        }
    }

    // ─────────────────────────────────────────────
    post {
    // ─────────────────────────────────────────────
        success {
            echo """
            ╔══════════════════════════════════════╗
            ║   ✅  Pipeline Completed Successfully  ║
            ║   Build #${env.BUILD_NUMBER}                  ║
            ╚══════════════════════════════════════╝
            """
        }
        failure {
            echo """
            ╔══════════════════════════════════════╗
            ║   ❌  Pipeline FAILED                  ║
            ║   Build #${env.BUILD_NUMBER}                  ║
            ║   Check logs above for details.       ║
            ╚══════════════════════════════════════╝
            """
        }
        always {
            echo 'Cleaning workspace...'
            cleanWs()
        }
    }
}
