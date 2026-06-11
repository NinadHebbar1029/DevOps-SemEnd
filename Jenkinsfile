pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'
        DOCKER_IMAGE = 'yourdockerhubusername/ml-pro-app:latest'
        SONAR_PROJECT_KEY = 'ml-pro-app'
    }

    stages {
        // Note: 'Checkout SCM' is automatically handled by the Declarative Pipeline

        stage('Git Version Check') {
            steps {
                echo 'Checking Git Version...'
                sh 'git --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing project dependencies...'
                sh 'pip install -r requirements.txt'
                dir('frontend') {
                    sh 'npm install'
                }
            }
        }

        stage('OWASP Dependency Check') {
            steps {
                echo 'Running OWASP Dependency Check...'
                // Assuming the Dependency-Check plugin is installed in Jenkins
                dependencyCheck additionalArguments: '--scan ./ --format XML --format HTML', odcInstallation: 'DP-Check'
            }
        }

        stage('Publish OWASP Report') {
            steps {
                echo 'Publishing OWASP Dependency Check Report...'
                dependencyCheckPublisher pattern: 'dependency-check-report.xml'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'Running SonarQube Analysis...'
                // Assuming SonarQube scanner is configured
                withSonarQubeEnv('SonarQube') {
                    sh "sonar-scanner -Dsonar.projectKey=${SONAR_PROJECT_KEY} -Dsonar.sources=."
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                echo 'Pushing Docker Image...'
                withCredentials([usernamePassword(credentialsId: env.DOCKER_CREDENTIALS_ID, passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin"
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Deploy Container') {
            steps {
                echo 'Deploying Container...'
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            echo 'Executing Post Actions...'
            cleanWs() // Clean the workspace after the build finishes
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
