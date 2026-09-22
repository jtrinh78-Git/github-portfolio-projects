# Authentication & Security API

A FastAPI authentication project demonstrating password hashing, JWT authentication, and protected API routes.

## Features

- User registration
- Argon2 password hashing
- Password verification
- JWT token generation
- Bearer token authentication
- Protected API endpoint
- Invalid token handling
- HTTP 401 authentication responses

## Technologies

- Python
- FastAPI
- Pydantic
- pwdlib
- Argon2
- PyJWT
- Uvicorn

## Authentication Flow

1. A user registers with a username and password.
2. The password is hashed with Argon2 before storage.
3. The user logs in with their credentials.
4. The submitted password is verified against the stored hash.
5. A successful login generates a signed JWT.
6. The JWT is sent using Bearer authentication.
7. The protected endpoint verifies and decodes the JWT.
8. Valid tokens receive protected data.
9. Missing or invalid credentials receive HTTP 401 responses.

## Endpoints

### POST /register

Registers a user and stores a hashed password.

### POST /login

Verifies the user's credentials and returns a JWT access token.

### GET /protected

Requires a valid Bearer JWT before returning protected data.

## Security Notes

Passwords are never stored as plaintext.

The secret key used in this project is intentionally a learning/demo value. Production applications should load secrets securely from environment variables or a secrets-management system rather than hard-coding them in source code.

## Purpose

This project demonstrates the authentication layer commonly used in larger API and AI applications.