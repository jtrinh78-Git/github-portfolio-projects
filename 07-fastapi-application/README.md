# FastAPI Application

A REST API built with Python and FastAPI to practice backend API development, HTTP methods, routing, request validation, and interactive API documentation.

## Features

- GET endpoints
- POST endpoint
- PUT endpoint
- DELETE endpoint
- Path parameters
- Query parameters
- JSON request bodies
- Pydantic data validation
- Automatic Swagger API documentation

## API Endpoints

- `GET /` — Returns a basic welcome message
- `GET /hello` — Returns a fixed greeting
- `GET /hello/{name}` — Demonstrates a path parameter
- `GET /search?name=` — Demonstrates a query parameter
- `GET /customers` — Returns sample customer data
- `POST /customers` — Accepts and validates customer data
- `PUT /customers/{customer_id}` — Accepts an ID and updated customer data
- `DELETE /customers/{customer_id}` — Demonstrates deletion endpoint behavior

## Customer Model

Customer request bodies require:

- `name`
- `email`

Both values must be strings.

## Running the Application

Install the dependencies:

    pip3 install fastapi uvicorn

Start the development server:

    uvicorn main:app --reload --port 8001

Open the interactive API documentation:

    http://127.0.0.1:8001/docs

## Concepts Learned

- FastAPI application creation
- REST API endpoints and routes
- HTTP GET, POST, PUT, and DELETE
- Route matching
- Path and query parameters
- Python type annotations
- JSON request and response bodies
- Pydantic models and validation
- HTTP status codes
- Swagger/OpenAPI documentation
- Uvicorn development server
- CRUD concepts through HTTP

## Bugs and Lessons

- `FastAPI` is the class; `FastAPI()` creates the application instance.
- FastAPI applications are served using Uvicorn rather than simply running `python3 main.py`.
- Port 8000 was already occupied, so the application was run on port 8001.
- Command-line flags such as `--reload` require the leading dashes.
- Incomplete decorators, functions, and dictionaries can cause syntax or indentation errors.
- Auto Save combined with Uvicorn reload can trigger errors while code is still being typed.
- Pydantic automatically validates incoming request bodies.
- Missing required customer data produced a `422` validation response.
- A successful endpoint response does not prove that database data changed.
- The current customer data is hard-coded and is not persisted.

## Next Step

The next project connects a FastAPI application to a database so the API can create, retrieve, update, and delete real persistent records.