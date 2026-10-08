pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Code checked out from GitHub'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t digital-payment-app:latest .'
            }
        }

        stage('Test Docker Image') {
            steps {
                bat 'docker images digital-payment-app'
            }
        }

       stage('Deploy to Kubernetes') {
    steps {
        bat 'set KUBECONFIG=C:\\ProgramData\\Jenkins\\.kube\\config && kubectl apply -f k8s/deployment.yaml'
        bat 'set KUBECONFIG=C:\\ProgramData\\Jenkins\\.kube\\config && kubectl apply -f k8s/service.yaml'
    }
}

        stage('Check Deployment') {
    steps {
        bat 'set KUBECONFIG=C:\\ProgramData\\Jenkins\\.kube\\config && kubectl get pods'
        bat 'set KUBECONFIG=C:\\ProgramData\\Jenkins\\.kube\\config && kubectl get services'
    }
}
    }
}