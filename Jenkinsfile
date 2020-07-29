properties([disableConcurrentBuilds()])

pipeline {
    agent { label 'master' }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }
    stages {
//         stage ('Building ticketland_test_image') {
//             steps {sh 'docker build -t ticketland_test_image .'}
//         }
//         stage ('Removing ticketland_test_container') {
//             steps {sh 'docker rm ticketland_test_container'}
//         }
//         stage ('Creating ticketland_test_container') {
//             steps {sh 'docker create --name ticketland_test_container -v /logs/allure-log:/logs/allure-results ticketland_test_image'}
//         }
//         stage ('Starting ticketland_test_container') {
//             steps {sh 'docker start -a ticketland_test_container'}
//         }
        stage ('Install requirements') {
            steps {sh 'pyton3 install -r requirements.txt'}
        }
        stage ('Collecting allure report') {
            steps {sh 'pytest -v tests/test_login_page.py --alluredir=logs/allure-log'}
        }
    }

    post {
        always {
            script {
                allure ([
                includeProperties: false,
                jdk: '',
                reportBuildPolicy: 'ALWAYS',
                report: 'Otus-Python-QA-Final-Project-Ticketland.ru/allure-report',
                results: [[path: 'Otus-Python-QA-Final-Project-Ticketland.ru/allure-results']]])
            }
        }
    }
}