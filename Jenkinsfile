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
                # Run tests using venv python
                ./${VENV_DIR}/bin/python -m pytest test_app.py
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
