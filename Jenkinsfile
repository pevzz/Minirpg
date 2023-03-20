pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                pip install tabulate
                pip install inquirer
                pip install flask
            }
        }
           stage('Play') {
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
