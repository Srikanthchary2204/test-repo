pipeline {
    agent any

    stages {
        stage('creating virtual env') {
            steps {
                script{r=sh( script : '''
                    #!/bin/bash
                    bash rm -rf venv
                    bash sh python3 -mvenv venv
                    bash source venv/bin/activate
                    bash pip install -r requirements.txt''',)
                }
                
            }
        }
    }
    stages {
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
