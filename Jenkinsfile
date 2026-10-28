pipeline {
    agent any

    options {
        timestamps()
    }

    environment {
        IMAGE_NAME = 'msc-ds-cicd-app'
        CONTAINER_NAME = 'msc-ds-cicd-app'
        APP_PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out successfully.'
            }
        }

        stage('Build and Test') {
            steps {
                sh '''
                    python3 --version
                    python3 -m unittest -v test_app.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                      -t ${IMAGE_NAME}:${BUILD_NUMBER} \
                      -t ${IMAGE_NAME}:latest .
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker rm -f ${CONTAINER_NAME} || true

                    docker run -d \
                      --name ${CONTAINER_NAME} \
                      -p 5000:5000 \
                      ${IMAGE_NAME}:${BUILD_NUMBER}

                    docker ps
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    docker inspect -f '{{.State.Running}}' \
                      ${CONTAINER_NAME}
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: CI/CD pipeline completed.'
        }
        failure {
            echo 'FAILURE: Check the console output.'
        }
    }
}