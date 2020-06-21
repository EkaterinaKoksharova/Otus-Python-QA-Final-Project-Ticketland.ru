pipeline {
    agent {label 'slave'}
    stages {
        stage ('Running autotests') {
            steps {
                sh 'docker build -t ticketland_test . && docker run ticketland_test'
            }
        }
    }
}