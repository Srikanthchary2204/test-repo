pipeline {
    agent any
    stages {
        stage('creating virtual env') {
            steps {
                bat 'run_wrapper.bat'
                bat 'pip install -r requirements.txt'
                
            }
                
        }
        stage('calling codes.py') {
            steps {
                bat 'python3 codes.py'
                echo "called: codes.py"
                
            }
                
        }
    }
}

