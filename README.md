# Setting Up a Declarative Jenkins Pipeline for a Demo Application

## Introduction

A **Declarative Jenkins Pipeline** is a structured and readable way to define CI/CD workflows as code. It simplifies pipeline creation, maintenance, and version control by using a clear syntax.

This project demonstrates how to configure a **Jenkins Declarative Pipeline** to:
- Connect a Jenkins agent node
- Perform code quality checks
- Build a Docker image
- Deploy a containerized demo application

---

## Pre-requisites

Ensure the following are available before starting:

- Ubuntu EC2 instance up and running
- Jenkins installed and accessible
- Docker installed on Jenkins agent node
- Java (OpenJDK 11)
- GitHub repository containing:
  - Dockerfile
  - requirements.txt
  - Application source code

---

## Step-by-Step Implementation

### Step 1: Connect VM Node to Jenkins

#### 1. Install Java (if not already installed)

```bash
sudo apt update
sudo apt install openjdk-11-jdk
```

#### 2. Set Up Jenkins Node   

1. Open the Jenkins Dashboard

2. Navigate to: Manage Jenkins → Nodes → New Node
3. Add a new node with the required configuration and save it.

<img width="1024" height="266" alt="image" src="https://github.com/user-attachments/assets/3dfe6d46-2e53-42da-9e6f-5344cfa6055c" />
<img width="1024" height="179" alt="image" src="https://github.com/user-attachments/assets/46c64568-bab1-43a4-84d0-65916dd1af7d" />

<img width="1024" height="483" alt="image" src="https://github.com/user-attachments/assets/f90980e9-6a68-4155-abb1-bed18626876b" />


<img width="1024" height="442" alt="image" src="https://github.com/user-attachments/assets/1fdce0bf-b584-4170-98ad-a1bc8bc36147" />

#### 3. Connect the Node to Jenkins
Run the following commands on the agent node:
```bash
curl -sO http://<JENKINS_URL>/jnlpJars/agent.jar
java -jar agent.jar -jnlpUrl <JENKINS_URL>/computer/<NODE_NAME>/jenkins-agent..jnlp -secret <SECRET> -workDir "/home/ubuntu/jenkins"
```
Replace <JENKINS_URL>, <NODE_NAME>, and <SECRET> with your Jenkins-specific values.

###  Step 2: Create and Configure the Pipeline

1. Open Jenkins Dashboard
2. Create a new pipeline job:
 - Navigate to New Item > Pipeline and name your pipeline.
 - In the pipeline configuration, select the Pipeline script option.
 - Copy and paste the following pipeline script:
## Jenkins Declarative Pipeline Script

```bash
pipeline {
    agent {
        node {
            label 'linuxnode'
        }
    }

    environment {
        IMAGE_TAG = 'latest'
        IMAGE_NAME = 'demo'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(
                    branches: [[name: '*/main']],
                    extensions: [],
                    userRemoteConfigs: [[
                        url: 'https://github.com/priyakalidaspawar/Jenkins.git'
                    ]]
                )
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    def pylintThreshold = 3
                    def pylintCommand = """
                        /usr/bin/python3 -m pylint \
                        --fail-under=${pylintThreshold} \
                        "/home/kube/jenkins/workspace/demo/src/app.py"
                    """
                    sh pylintCommand

                    def pylintExitCode = sh(
                        script: 'echo $?',
                        returnStatus: true
                    )

                    if (pylintExitCode == 0) {
                        echo "Linting Success"
                    } else {
                        echo "Linting failed"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dir('src') {
                        docker.build(
                            "${IMAGE_NAME}:${IMAGE_TAG}",
                            "-f Dockerfile ."
                        )
                    }
                }
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    docker.image(
                        "${IMAGE_NAME}:${IMAGE_TAG}"
                    ).run('-d -p 5000:5000')
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
```
### Step 3: Verify Docker Images and Containers

1. Verify Docker Image

```bash
   docker images
```
Ensure the following image is available: 
``` bash
demo:latest
```
2. Verify Running Container
```bash
docker ps
```

### Step 4: Access the Application

1. Open a web browser
2. Navigate to:
```bash
http://<AGENT_NODE_IP>:5000
```
If the application loads successfully, the deployment is complete.  

