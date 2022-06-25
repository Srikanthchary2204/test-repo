pipeline {
    agent any
    stages {
        stage('run codes') {
            steps {
                bat "pip install -r requirements.txt"
                bat 'python3 codes.py'
                cleanWs()
                
            }
                
        }
        
    }
}

