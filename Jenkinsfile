pipeline {
	agent any
	stages {
		stage('build') {
			steps {
				sh 'python3 --version'

				sh 'python3 -m venv .'
				sh 'chmod +x ./bin/activate'
				sh './bin/activate'

				sh './bin/pip3 install -r requirements.txt'
			}
			stage('Test') {
    			steps {
        			sh '''
            			. venv/bin/activate
            			pip install pytest pytest-timeout
            			pytest tests/ --junitxml=test-results.xml -v --timeout=30
        			'''
    		}
    post {
        always {
            junit 'test-results/*.xml'
        }
    }
}

		}
		stage('deploy') {
			steps {	
				sh './bin/python3 src/app.py' 
			}
		}
	}
}
