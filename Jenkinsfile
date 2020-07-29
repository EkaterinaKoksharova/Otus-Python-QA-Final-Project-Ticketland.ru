properties([disableConcurrentBuilds()])

pipeline {
    agent { label 'master' }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }
    stages {
        stage ('Install requirements') {
            steps {sh 'pip3 install -r requirements.txt'}
        }
        stage ('Collecting allure report') {
            steps {sh 'pytest -v tests/test_login_page.py --alluredir=/var/jenkins_home/workspace/Otus-Python-QA-Final-Project-Ticketland.ru/target/allure-results'}
        }
    }

    post {
        always {
            script {
                allure ([
                includeProperties: false,
                jdk: 'InheritFromJob',
                reportBuildPolicy: 'ALWAYS',
                report: 'target/allure-report',
                results: [[path: 'target/allure-results']]])
            }
        }
    }
}