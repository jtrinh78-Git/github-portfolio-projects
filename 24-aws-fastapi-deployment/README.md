
# AWS EC2 FastAPI Deployment

## Overview
Deployed an existing Python FastAPI portfolio application to an Amazon Linux 2023 EC2 instance. Configured a systemd service to run the API and Nginx as a reverse proxy.

## Architecture
GitHub repository → AWS EC2 (Amazon Linux 2023) → Nginx (port 80) → FastAPI/Uvicorn (127.0.0.1:9000)

## Technologies
- AWS EC2
- Amazon Linux 2023
- Python and FastAPI
- Uvicorn
- Nginx
- systemd
- Git and GitHub

## Deployment Steps
1. Launched an EC2 instance running Amazon Linux 2023.
2. Connected through EC2 Instance Connect.
3. Cloned the existing GitHub portfolio repository.
4. Created a Python virtual environment and installed FastAPI and Uvicorn.
5. Configured a systemd service for the FastAPI application.
6. Configured Nginx to proxy HTTP requests to the application on localhost port 9000.
7. Validated the Nginx configuration and reloaded the service.
8. Tested the application through Nginx.

## Verification

Command:

```bash
curl -i http://127.0.0.1/hello/Joseph
```

Observed result:

```text
HTTP/1.1 200 OK
Server: nginx/1.30.5

{"message":"Hello Joseph"}
```

Confirmed that the FastAPI systemd service was enabled for automatic startup.

## Security and Scope
- FastAPI listens on 127.0.0.1:9000, behind Nginx.
- The reverse proxy was verified locally on the EC2 instance.
- Public browser access, HTTPS, authentication, and production hardening have not been completed or verified.
- The EC2 instance can be stopped when not in use to reduce compute charges.

## Future Improvements
- Add automated deployment using GitHub Actions.
- Introduce HTTPS and a domain name.
- Review API authentication and exposure before enabling public access.
- Add deployment monitoring and operational checks.
  