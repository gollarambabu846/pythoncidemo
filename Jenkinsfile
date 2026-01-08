pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
        FLASK_APP = "app.py"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Checking out code from GitHub..."
                git branch: 'main', url: 'https://github.com/gollarambabu846/pythoncidemo.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                echo "Creating virtual environment and installing dependencies..."
                sh """
                    python3 -m venv ${VENV_DIR}
                    ${VENV_DIR}/bin/pip install --upgrade pip
                    ${VENV_DIR}/bin/pip install -r requirements.txt
                """
            }
        }

        stage('Run Flask App') {
            steps {
                echo "Starting Flask app..."
                sh """
                    # Run Flask in background
                    nohup ${VENV_DIR}/bin/python -m flask run --host=0.0.0.0 --port=5000 > flask.log 2>&1 &
                    sleep 5
                    curl http://localhost:5000
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running pytest tests..."
                sh """
                    export PYTHONPATH=\$PWD
                    ${VENV_DIR}/bin/python -m pytest test_app.py
                """
            }
        }
    }

    post {
        success {
            echo "Build and tests completed successfully!"
        }
        failure {
            echo "Build or tests failed!"
        }
    }
}
