# Project 25 — AWS Docker FastAPI Deployment

## Project Overview

Containerized an existing Python FastAPI application using Docker and deployed it to an Amazon EC2 Linux server.

This project demonstrates hands-on cloud engineering skills, including Docker image creation, container execution, API testing, Linux server administration, and GitHub version control.

## Technologies

- Amazon Web Services (AWS EC2)
- Amazon Linux 2023
- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- Docker
- Git and GitHub

## Application Features

The FastAPI application demonstrates:

- GET endpoints and JSON responses
- URL path parameters
- Query parameters
- POST requests with Pydantic validation
- PUT and DELETE request handlers
- Automatic OpenAPI documentation

Customer operations are demonstration endpoints and do not persist data to a database.

## Docker Configuration

The Dockerfile:

1. Uses the official Python 3.12 slim image.
2. Sets `/app` as the working directory.
3. Copies `main.py` into the image.
4. Installs FastAPI and Uvicorn.
5. Starts Uvicorn on port 8001.

## Deployment Commands

From the project directory on an EC2 server with Docker installed:

```bash
sudo docker build -t portfolio-fastapi:v1 .
sudo docker run -d --name portfolio-fastapi -p 127.0.0.1:8001:8001 portfolio-fastapi:v1
```

These commands assume the container name and host port are available.

## Verification

Test the running application from the EC2 server:

```bash
curl http://127.0.0.1:8001/
curl http://127.0.0.1:8001/hello/Joseph
curl http://127.0.0.1:8001/openapi.json
```

The original application was successfully built and tested in Docker on AWS EC2.

The Project 25 folder contains a copy of the tested application and Dockerfile. This folder has not yet been independently deployed.

## Security

The Docker container binds to `127.0.0.1` on the EC2 host, restricting access to the server itself. This exercise does not expose the API publicly.

## Engineering Skills Demonstrated

- AWS EC2 administration
- Linux command-line operations
- Docker image building
- Container deployment
- REST API testing
- GitHub authentication and version control
- Remote commit verification

## Related Portfolio Project

Project 07 — FastAPI Application provided the original application used for this AWS Docker deployment exercise.
