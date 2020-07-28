properties([disableConcurrentBuilds()])

pipeline {
    agent { label 'master' }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }
    stages {
        stage ('Building ticketland_test_image') {
            steps {sh 'docker build -t ticketland_test_image .'}
        }
        stage ('Removing ticketland_test_container') {
            steps {sh 'docker rm ticketland_test_container'}
        }
        stage ('Creating ticketland_test_container') {
            steps {sh 'docker create --name ticketland_test_container -v /logs/allure-log:/logs/allure-results ticketland_test_image'}
        }
        stage ('Starting ticketland_test_container') {
            steps {sh 'docker start -a ticketland_test_container'}
        }
        stage ('Running autotests') {
            steps {sh 'ls'}

            post {
                always {
                    script {
                        allure ([
                        includeProperties: false,
                        jdk: '',
                        reportBuildPolicy: 'ALWAYS',
                        report: '/target/allure-report',
                        results: [[path: '/target/allure-results']]])
                    }
                }
            }
        }
    }
}