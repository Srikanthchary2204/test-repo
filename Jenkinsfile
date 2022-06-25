pipeline {
    agent any
    stages {
        stage('run codes') {
            steps {
                bat "pip install requirements.txt"
                bat 'python3 codes.py'
                cleanWs()
                
            }
                
        }
        
    }
}

