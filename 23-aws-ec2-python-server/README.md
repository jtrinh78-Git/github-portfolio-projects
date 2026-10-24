# AWS Project 01 — EC2 Linux Python Server

## Project Overview

This project demonstrates how to launch and use an Amazon EC2 Linux server to run a Python application in the cloud.

The goal is to practice foundational AWS cloud engineering skills, including Linux administration, secure remote access, Python execution, and Git version control.

## Technologies Used

- Amazon Web Services (AWS)
- Amazon EC2
- Amazon Linux 2023
- Python 3
- Linux Terminal
- SSH (Secure Shell)
- Git
- GitHub
- GNU nano
- SCP (Secure Copy)

## Architecture

```text
Mac Computer
    |
    | SSH Connection
    v
AWS EC2 Instance
    |
    | Amazon Linux 2023
    v
Python 3
    |
    v
app.py
    |
    v
Hello, from my AWS cloud server!
```

The Mac connects securely to the AWS EC2 instance using SSH. Python runs on the remote Linux server and executes the application.

## Project Structure

```text
23-aws-ec2-python-server/
├── app.py
└── README.md
```

The project was originally developed in the `aws-python-practice` directory on the EC2 instance and then transferred into the local GitHub portfolio.

## Python Application

The application contains:

```python
print("Hello, from my AWS cloud server!")
```

The program prints a message when executed using Python 3.

## Running the Application

### 1. Connect to the EC2 Instance

Use SSH from a terminal with an authorized private key:

```bash
ssh -i /path/to/your-private-key.pem ec2-user@YOUR_EC2_PUBLIC_IP
```

Replace the example key path and public IP address with your own values.

### 2. Navigate to the Project Directory

On the EC2 server:

```bash
cd ~/aws-python-practice
```

### 3. Run the Python Application

```bash
python3 app.py
```

Expected output:

```text
Hello, from my AWS cloud server!
```

### 4. Run the Application Locally

After downloading the project, navigate to the local project directory and run:

```bash
python3 app.py
```

The application was successfully tested on both AWS Linux and macOS.

## Git Version Control

This project uses Git to track source code changes.

Commands practiced:

```bash
git init
git branch -m main
git add app.py
git commit -m "Add first AWS Python application"
git status
git log -1
```

The initial commit was amended to use the correct developer identity.

The project documentation was committed separately on the EC2 server.

The project files were then copied into the existing GitHub portfolio repository, which maintains its own Git history.

## Secure File Transfer

SCP was used to transfer the Python application and README from AWS EC2 to the local Mac.

Example:

```bash
scp -i /path/to/your-private-key.pem ec2-user@YOUR_EC2_PUBLIC_IP:/home/ec2-user/aws-python-practice/app.py /path/to/local/project/
```

This process transfers files over an SSH connection.

The EC2 repository's hidden `.git` directory was not copied into the portfolio repository.

## Security Practices

- SSH private key stored on the local Mac.
- Private key permissions restricted to the owner.
- Remote access performed using SSH.
- No private keys or credentials included in source code.
- EC2 security group access should be restricted to trusted IP addresses.
- AWS resources should be stopped or removed when not needed to control costs.
- SSH client reported that the connection did not negotiate a post-quantum-resistant key exchange.

Never upload private SSH keys, passwords, or AWS credentials to GitHub.

Stopping an EC2 instance does not necessarily eliminate every AWS charge. Storage and other allocated resources may still incur costs.

## Skills Demonstrated

- Launching an AWS EC2 Linux instance
- Connecting securely through SSH
- Navigating the Linux filesystem
- Understanding Linux file permissions
- Creating and editing files using nano
- Running Python on a remote cloud server
- Initializing and managing a Git repository
- Creating Git commits and verifying commit history
- Writing technical project documentation
- Transferring files securely using SCP
- Running the same Python application on Linux and macOS
- Preparing a cloud engineering project for GitHub

## Verification

Completed during the hands-on exercise:

- EC2 instance reached running state.
- AWS status checks passed.
- SSH connection established.
- Python application executed successfully on AWS.
- Git repository initialized on the main branch.
- Initial commit created and author identity verified.
- README documentation created and committed.
- Git working tree confirmed clean on AWS.
- SSH session disconnected successfully.
- Python application transferred to the Mac.
- README transferred to the Mac.
- Both transferred files verified locally.
- Python application executed successfully on macOS.

## Future Improvements

- Add a Python virtual environment.
- Build a FastAPI web application.
- Expose an HTTP endpoint with appropriate security controls.
- Containerize an application using Docker.
- Add automated tests and CI/CD.
- Explore production-style AWS deployment and monitoring.
- Learn AWS IAM, CloudWatch, and cost monitoring.
- Deploy machine learning applications to AWS.
- Explore Microsoft Azure cloud services.

## Project Status

**Phase 1:** EC2, Linux, Python, and Git foundations completed.

**Phase 2:** Documentation completed. Portfolio publication in progress.