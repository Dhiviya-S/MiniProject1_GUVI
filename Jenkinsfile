pipeline {
    agent any

    environment {
        PYTHON = '/Library/Frameworks/Python.framework/Versions/3.11/bin/python3'  // Use actual path from `which python3`
    }

    stages {
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/Dhiviya-S/MiniProject1_GUVI'
            }
        }

        stage('Run Tests') {
            steps {
                dir('MiniProject1') {
                    sh 'python3 Tests/'
                }
        }
    }
}
