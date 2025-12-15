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

