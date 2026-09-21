# FastAPI + SQLite CRUD API

A REST API built with FastAPI, Python, and SQLite that demonstrates persistent CRUD operations.

## Features

- Create customers with POST
- Read customers with GET
- Update customers with PUT
- Delete customers with DELETE
- Persist customer data with SQLite
- Validate request bodies with Pydantic
- Return 404 errors for nonexistent customers
- Return 422 errors for invalid request bodies

## Technologies

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

## API Endpoints

- `GET /customers` - Get all customers
- `POST /customers` - Create a customer
- `PUT /customers/{id}` - Update a customer
- `DELETE /customers/{id}` - Delete a customer

## Concepts Learned

- Connecting FastAPI routes to a SQLite database
- Executing SQL from Python
- Using SQL parameter placeholders
- Persisting changes with `commit()`
- Building persistent CRUD operations
- Using `cursor.rowcount` to detect missing records
- Raising `HTTPException` for 404 responses
- Request validation with Pydantic
- Testing APIs with Swagger UI

## Bugs and Lessons

A successful HTTP response does not automatically prove that a database operation changed data. CRUD operations were verified with follow-up GET requests.

SQLite initially raised a thread error because the database connection was created in one thread and used in another. For this learning project, the connection was configured with `check_same_thread=False`.

UPDATE and DELETE initially returned successful responses for IDs that did not exist. This was fixed by checking `cursor.rowcount` and returning a 404 response when no rows were affected.