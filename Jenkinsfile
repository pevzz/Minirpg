pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'python main.py'
            }
        }
           stage('Score') {
            steps {
                bat 'python Score.py'
            }
        }
    }
}
