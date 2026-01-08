pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {

        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/gollarambabu846/pythoncidemo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                # Create virtual environment
                python3 -m venv ${VENV_DIR}

                # Upgrade pip inside venv
                ./${VENV_DIR}/bin/pip install --upgrade pip

                # Install required packages
                ./${VENV_DIR}/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
                # Run the app using venv python
                ./${VENV_DIR}/bin/python app.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
             ./venv/bin/python -m flask run --host=0.0.0.0 --port=5000 &
               sleep 5  # wait a few seconds for the server to start
               curl http://localhost:5000  # check if server is running
                '''
            }
        }
    }

    post {
        always {
            echo "Build finished"
        }
        success {
            echo "Build succeeded!"
        }
        failure {
            echo "Build failed!"
        }
    }
}
