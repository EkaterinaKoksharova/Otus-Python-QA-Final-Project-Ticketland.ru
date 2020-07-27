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
            steps {sh 'docker run ticketland_test'}

            post {
                always {
                    script {
                        allure ([
                        includeProperties: false,
                        jdk: '',
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'logs/allure-report']]])
                    }
                }
            }
        }
    }
}

// pipeline {
//     agent any
//     options {
//         buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
//         timestamps()
//     }
//     stage("create docker image") {
//             steps {
//                 echo "start building image"
//                 sh "docker build - < Dockerfile"
//             }
//         }
//     stages {
//         stage("memory information") {
//             steps {
//                 sh "free -h"
//             }
//         }
//         stage('lint') {
//             steps {
//                 sh 'flake8 .'
//             }
//         }
//         stage('tests') {
//             steps {
//                 sh "pytest -v -s"
//             }
//         }
//         post {
//             always {
//                 script {
//                     allure ([
//                     includeProperties: false,
//                     jdk: '',
//                     reportBuildPolicy: 'ALWAYS',
//                     results: [[path: 'python-selenium/allure-results']]])
//                 }
//         }
//     }
//     }
//   }
