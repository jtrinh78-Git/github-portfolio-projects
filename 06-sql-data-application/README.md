# SQL Data Application

A Python application that uses SQLite to create and manage customer data while demonstrating the core CRUD operations: Create, Read, Update, and Delete.

## Features

* Connects Python to a SQLite database
* Creates a customers table
* Inserts customer records
* Reads customer data with SELECT
* Filters records with WHERE
* Updates existing customer information
* Deletes customer records
* Saves database changes with commit()
* Retrieves query results with fetchall()
* Closes the database connection safely

## Concepts Learned

* SQLite databases
* Database tables, columns, and rows
* Primary keys
* SQL CRUD operations
* Parameterized SQL queries
* Python sqlite3 module
* Database connections and cursors
* execute() vs fetchall()
* commit() and database persistence
* WHERE filtering
* Opening and closing database connections

## Bugs and Lessons

* Learned that SQL commands must be passed through cursor.execute() rather than written directly as Python code.
* Fixed SQL syntax errors caused by invalid placeholder text and missing parentheses.
* Learned the difference between execute() and fetchall().
* Discovered that repeatedly running an INSERT statement can create duplicate database rows.
* Used DELETE with WHERE to safely remove duplicate records.
* Learned that UPDATE uses SET to specify what changes and WHERE to specify which row changes.
* Learned that relative database paths depend on the terminal's current working directory.
* Learned to commit database changes before closing the connection.

## How to Run

From the project directory, run:

```bash
python3 sql_app.py
```
