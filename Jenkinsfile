pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/tnraja/rajav-flask-cicd-assignment.git
            }
        }
        
        stage('Build') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Lint') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install flake8
                    flake8 . --count --exit-zero
                '''
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install pytest
                    pytest tests/ --junitxml=test-reports.xml -v
                '''
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
            }
        }
        
        stage('Deploy Staging') {
            when { branch 'main' }
            steps {
                sh '''
                    echo "🚀 Deploying to Render Staging..."
                    echo "Staging URL: https://flask-staging.onrender.com"
                '''
            }
        }
    }
    
    post {
        success {
            emailext (
                to: 'tn69raja@gmail.com',
                subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Pipeline passed! ${env.BUILD_URL}",
                mimeType: 'text/html'
            )
        }
        failure {
            emailext (
                to: 'tn69raja@gmail.com',
                subject: "FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Pipeline failed! ${env.BUILD_URL}",
                mimeType: 'text/html'
            )
        }
    }
}
