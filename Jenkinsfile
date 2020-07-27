properties([disableConcurrentBuilds()])

pipeline {
    agent { label 'master' }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }
    stages {
        stage ('Python version') {
            steps {sh 'python3 -v'}
        }
        stage ('Install pip3') {
            steps {sh 'apt-get install python3-pip -y'}
        }
        stage ('Install requirements') {
            steps {sh 'pip3 install -r requirements.txt'}
        }
        stage ('Running autotests') {
            steps {sh 'pytest -v tests/test_login_page.py --alluredir=logs/allure-report'}

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

// properties([disableConcurrentBuilds()])
//
// pipeline {
//     agent { label 'master' }
//     options {
//         buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
//         timestamps()
//     }
//     stages {
//         stage ('Buildine image with tests') {
//             steps {sh 'docker build -t ticketland_test .'}
//         }
//         stage ('Running autotests') {
//             steps {sh 'docker run -v /Users/zsergey/PycharmProjects/Otus-Python-QA-Final-Project-Ticketland.ru/logs:/var/jenkins_home/workspace/TestOtus/logs/allure-report ticketland_test'}
//
//             post {
//                 always {
//                     script {
//                         allure ([
//                         includeProperties: false,
//                         jdk: '',
//                         reportBuildPolicy: 'ALWAYS',
//                         report: 'logs/allure-report',
//                         results: [[path: 'logs/allure-report']]])
//                     }
//                 }
//             }
//         }
//     }
// }