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
        stage ('Creating ticketland_test_container') {
            steps {sh 'docker create -name ticketland_test_container icketland_test_image.'}
        }
        stage ('Starting ticketland_test_container') {
            steps {sh 'docker start -a ticketland_test_container'}
        }
        stage ('Running autotests') {
            steps {sh 'docker run -v /Users/zsergey/PycharmProjects/Otus-Python-QA-Final-Project-Ticketland.ru/logs/allure-log:/var/jenkins_home/workspace/TestOtus/logs/allure-report ticketland_test'}

            post {
                always {
                    script {
                        allure ([
                        includeProperties: false,
                        jdk: '',
                        reportBuildPolicy: 'ALWAYS',
                        report: 'logs/allure-report',
                        results: [[path: 'logs/allure-results']]])
                    }
                }
            }
        }
    }
}