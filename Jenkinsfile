properties([disableConcurrentBuilds()])

pipeline {
    agent { label 'master' }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }
    stages {
        stage ('Buildine image with tests') {
            steps {sh 'docker build -t ticketland_test .'}
        }
        stage ('Running autotests') {
            steps {sh 'docker run -v logs/allure-report:logs/allure-report ticketland_test'}

            post {
                always {
                    script {
                        allure ([
                        includeProperties: false,
                        jdk: '',
                        reportBuildPolicy: 'ALWAYS',
                        report: 'logs/allure-report',
                        results: [[path: 'logs/allure-report']]])
                    }
                }
            }
        }
    }
}