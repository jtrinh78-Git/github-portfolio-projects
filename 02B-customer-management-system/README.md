# Customer Management System

A Python command-line customer management application using SQLite for persistent data storage.

## Features

- Add customers
- View all customers
- Search customers by name
- Update customer email addresses
- Delete customers
- Handle invalid menu choices
- Store customer data persistently with SQLite

## Technologies

- Python
- SQLite
- pathlib

## Concepts Practiced

- Python functions
- `if / elif / else`
- `while` loops
- SQL CRUD operations
- Parameterized SQL queries
- SQLite database connections
- `cursor.execute()`
- `fetchone()` and `fetchall()`
- `conn.commit()`
- `cursor.rowcount`
- Persistent database storage

## SQL CRUD Patterns

```text
CREATE TABLE → table → columns

INSERT INTO → table → columns → VALUES → values

SELECT → columns → FROM → table → WHERE → condition

UPDATE → table → SET → changes → WHERE → condition

DELETE FROM → table → WHERE → condition