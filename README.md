# DevOps Learning Vault 🚀

Welcome to my comprehensive DevOps portfolio! This repository documents my 12-week journey mastering modern cloud infrastructure, automation, and CI/CD pipelines.

## ️ Tech Stack & Skills
- **Cloud & IaC:** AWS, LocalStack, Terraform, Ansible
- **Containers & Orchestration:** Docker, Kubernetes (K8s)
- **CI/CD & Automation:** GitHub Actions, Bash Scripting, Python
- **Monitoring:** Custom Health Checks, Log Analysis
- **OS & Networking:** Linux (Ubuntu/CentOS), TCP/IP, DNS, Firewalls

## 📂 Repository Structure
- `linux-labs/`: Bash automation and log parsing scripts.
- `monitoring-labs/`: Python-based health monitoring agents.
- `server-labs/`: Nginx reverse proxy configurations.
- `iac-labs/`: Terraform and Ansible Infrastructure as Code.
- `.github/workflows/`: Automated CI/CD pipelines.

##  Capstone Project
The `capstone-pipeline.yml` is an end-to-end CI/CD pipeline that:
1. Spins up a LocalStack environment in the cloud.
2. Validates Terraform formatting and syntax.
3. Runs a `terraform plan` against a mock AWS environment.
4. Validates Python application code.

##  How to Run
Clone this repo and explore the folders! To run the LocalStack Terraform labs, ensure Docker is running and use the provided `main.tf` configurations.