pipeline {
    agent any

    stages {
        stage('creating virtual env') {
            steps {
                script{r=sh( script : '''
                    #!/bin/bash
                    rm -rf venv
                    python3 -mvenv venv
                    source venv/bin/activate
                    pip install -r requirements.txt''')
                }
                
            }
        }
        stage('calling run_wrapper.sh') {
            steps {
                sript{sh'''
                     #!bin/bash
                     set -ex
                     gsutil ls gs://demo1-348613/demotabl/
                     bash run_wrapper.sh'''


                }
                
                
            }
        }
    }
}
