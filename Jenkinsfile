pipeline {
    agent any

    stages {
        stage('Clone from GitHub') {
            steps {
                script {
                    // Clean workspace before cloning
                    deleteDir()

                    // Clone the GitHub repository
                    git 'https://github.com/devopshydclub/vprofile-project.git'
                }
            }
        }

        stage('Copy to Server') {
            steps {
                script {
                    // Create a destination directory on the Jenkins server
                    sh 'sudo mkdir -p /var/www/html'

                    // Set ownership and permissions on the destination directory
                    sh 'sudo chown -R jenkins:jenkins /var/www/html/'
                    sh 'sudo chmod -R u+w /var/www/html/'

                    // Use rsync to copy files while preserving ownership
                    sh 'sudo rsync -av --exclude=".git" ./ /var/www/html/'
                }
            }
        }
    }
}
