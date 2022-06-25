pipeline {
    agent any
    stages {
        stage('run codes') {
            steps {
                bat 'cd appdata/local/programs/python/python310/lib/site-packages'
                bat 'python3 codes.py'
                cleanWs()
                
            }
                
        }
        
    }
}

