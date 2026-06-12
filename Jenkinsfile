pipeline {
    agent any

    environment {
        // Project info
        PROJECT_NAME = 'mindease-chatbot'
        DOCKER_HUB_REPO = 'ninadhebbar1029/devops-semend'
        
        // =========================================================================
        // SECURE CREDENTIALS SETUP
        // We are now safely fetching the tokens you created in the Jenkins UI!
        // =========================================================================
        
        // This automatically creates DOCKER_CREDS_USR and DOCKER_CREDS_PSW
        DOCKER_CREDS = credentials('DockerhubToken')
        
        SONAR_PROJECT_KEY = 'mindease-chatbot'
        SONAR_TOKEN = credentials('SonarToken')
        
        VERCEL_TOKEN = credentials('VercelToken')
        
        GITHUB_TOKEN = credentials('GithubToken')
        
        // Keep your Render hook placeholder
        RENDER_DEPLOY_HOOK = 'https://api.render.com/deploy/srv-placeholder'
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
        timeout(time: 30, unit: 'MINUTES')
        timestamps()
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out branch: ${env.BRANCH_NAME ?: 'main'}"
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Node dependencies for Vercel CLI...'
                dir('frontend') {
                    bat 'npm ci --silent'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'Running SonarQube analysis...'
                bat "docker run --rm -v \"%CD%:/usr/src\" -e SONAR_TOKEN=%SONAR_TOKEN% sonarsource/sonar-scanner-cli -Dsonar.host.url=http://host.docker.internal:9000 -Dsonar.token=%SONAR_TOKEN% -Dsonar.projectKey=${SONAR_PROJECT_KEY} -Dsonar.sources=api.py,src -Dsonar.exclusions=**/node_modules/**,data/**,models/**,reports/**,frontend/**,**/__pycache__/**,src/train_models.py,src/evaluate_models.py,src/roc_auc.py -Dsonar.python.version=3.11"
            }
        }

        stage('OWASP Dependency Check') {
            steps {
                echo 'Running OWASP Dependency Check...'
                dependencyCheck(
                    additionalArguments: '''
                        --scan ./
                        --format XML
                        --format HTML
                        --out ./dependency-check-report
                        --exclude **/node_modules/**
                        --exclude **/__pycache__/**
                        --exclude **/models/**
                        --exclude **/data/**
                    ''',
                    odcInstallation: 'OWASP Dependency-Check'
                )
            }
        }

        stage('Build Docker Images') {
            parallel {
                stage('Build Backend') {
                    steps {
                        echo 'Building backend image...'
                        bat "docker build -t ${DOCKER_HUB_REPO}:backend-${env.BUILD_NUMBER} -t ${DOCKER_HUB_REPO}:backend-latest ."
                    }
                }
                stage('Build Frontend') {
                    steps {
                        echo 'Building frontend image...'
                        bat """
                            docker build ^
                              --build-arg VITE_API_URL=http://localhost:8000 ^
                              -t ${DOCKER_HUB_REPO}:frontend-${env.BUILD_NUMBER} ^
                              -t ${DOCKER_HUB_REPO}:frontend-latest ^
                              ./frontend
                        """
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing images to Docker Hub...'
                bat "echo %DOCKER_CREDS_PSW% | docker login -u %DOCKER_CREDS_USR% --password-stdin"
                
                bat "docker push ${DOCKER_HUB_REPO}:backend-${env.BUILD_NUMBER}"
                bat "docker push ${DOCKER_HUB_REPO}:backend-latest"
                
                bat "docker push ${DOCKER_HUB_REPO}:frontend-${env.BUILD_NUMBER}"
                bat "docker push ${DOCKER_HUB_REPO}:frontend-latest"
            }
        }

        stage('Deploy Backend → Render') {
            steps {
                echo 'Triggering Render deploy...'
                bat """
                    curl -s -X POST "${RENDER_DEPLOY_HOOK}" ^
                      -o NUL ^
                      -w "HTTP Status: %%{http_code}\\n" || exit 0
                """
            }
        }

        stage('Deploy Frontend → Vercel') {
            steps {
                echo 'Deploying to Vercel via CLI...'
                bat 'npx vercel deploy --prod --yes --token=%VERCEL_TOKEN%'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline Completed Successfully (Build #${env.BUILD_NUMBER})"
        }
        failure {
            echo "❌ Pipeline FAILED (Build #${env.BUILD_NUMBER})"
        }
        always {
            echo 'Cleaning workspace...'
            dependencyCheckPublisher(
                pattern: 'dependency-check-report/dependency-check-report.xml',
                failedTotalCritical: 1,
                unstableTotalHigh: 5
            )
            cleanWs()
            bat "docker rmi ${DOCKER_HUB_REPO}:backend-${env.BUILD_NUMBER} ${DOCKER_HUB_REPO}:frontend-${env.BUILD_NUMBER} || exit 0"
        }
    }
}
