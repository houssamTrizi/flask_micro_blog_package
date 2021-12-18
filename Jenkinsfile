pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    environment {
        HOME = "${env.WORKSPACE}"
    }
    stages {
        stage('install dependencies') {
            steps {
                sh 'python --version'
                sh 'python -m pip install --upgrade pip --user'
                sh 'python -m pip install -r requirements.txt --user --no-cache'
            }
        }
        stage('test'){
            steps{
                sh 'python -m pytest --version'
                sh 'python -m pytest tests'
            }
        }
    }
    post {
        always{
            cleanWs()
        }
    }
}
