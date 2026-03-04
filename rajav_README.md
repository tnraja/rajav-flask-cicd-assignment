# Complete CI/CD Pipeline Documentation

# Jenkins + GitHub Actions for Flask Application

Repo : https://github.com/tnraja/rajav-flask-cicd-assignment.git

Forked from : https://github.com/j-dax/simple-flask-jenkins.git

# Install Jenkins + Python

sudo apt update

sudo apt install openjdk-17-jre jenkins python3-pip git docker.io -y

sudo systemctl start jenkins && sudo systemctl enable jenkins

# Jenkins Admin ped read 

sudo cat /var/lib/jenkins/secrets/initialAdminPassword

# Jenkins URL
http://3.239.192.215:8080/

# Manage Jenkins → Manage Plugins → Available:
Pipeline
GitHub Integration  
Email Extension
Docker Pipeline

# Create Pipeline Job
New Item → "rajav_flaskapp_cicd_pipeline" → Pipeline → OK

Pipeline → Pipeline script from SCM:
- Git: https://github.com/tnraja/rajav-flask-cicd-assignment.git
- Script Path: Jenkinsfile

# Manage Jenkins → Configure System → Extended E-mail:
SMTP Server: smtp.gmail.com
Port: 587
Default Recipients: tn69raja@gmail.com

# Manage Jenkins → Configure System →  E-mailNotification:
SMTP Server: smtp.gmail.com
Port: 587
Default Recipients: tn69raja@gmail.com

# Output

# VM Structure 

<img width="1337" height="425" alt="image" src="https://github.com/user-attachments/assets/088023bf-fb96-4c75-b2a6-907d022ae580" />

# Github Action Workflows

<img width="1902" height="942" alt="image" src="https://github.com/user-attachments/assets/58294048-5bbf-4060-b578-a9f2e17a4507" />

# Jenkins Build page

<img width="1888" height="963" alt="image" src="https://github.com/user-attachments/assets/d810c622-134c-4865-b830-e20831ef33bf" />

# Email Notification

<img width="1902" height="921" alt="image" src="https://github.com/user-attachments/assets/c36705da-6d1c-4728-acf3-b391f44e2527" />

<img width="1872" height="943" alt="image" src="https://github.com/user-attachments/assets/c34f8a37-ace8-45c8-9061-82cd90485dae" />

