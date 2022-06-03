pipeline {
    agent any

    stages {
        stage('creating virtual env') {
            steps {
                script{r=bat( script : '''
                    python3 -mvenv venv
                    `source venv/bin/activate`
                    pip install -r requirements.txt''')
                }
                
            }
        }
        stage('calling run_wrapper.sh') {
            steps {
                sript{bat'''
                     set -ex
                     gsutil ls gs://demo1-348613/demotabl/
                     bash run_wrapper.sh'''


                }
                
                
            }
        }
    }
}
