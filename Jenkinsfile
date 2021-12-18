pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    environment {
        HOME = "${env.WORKSPACE}"
    }
    stages {
        stage('install dependencies') {
            steps {
                sh 'python --version'
                sh 'pip install --upgrade pip --user'
                sh 'pip install -r requirements.txt --user --no-cache'
            }
        }
        stage('test'){
            steps{
                sh 'pytest --version'
                sh 'pytest tests'
            }
        }
    }
    post {
        always{
            cleanWs()
        }
    }
}
