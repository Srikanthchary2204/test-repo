pipeline {
    agent any
    stages {
        stage('creating virtual env') {
            steps {
                bat 'run_wrapper.bat'
                
            }
                
        }
        stage('calling execute wapper') {
            steps {
                bat execute_wrapper.py
                bat echo "calling: execute wraper"
                
            }
                
        }
    }
}

