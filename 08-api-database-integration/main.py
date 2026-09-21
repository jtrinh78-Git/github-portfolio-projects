import sqlite3

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

class Customer(BaseModel):
    name: str
    email: str

connection = sqlite3.connect("customers.db", check_same_thread=False)

cursor = connection.cursor()

app = FastAPI()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS customer(
       id INTEGER PRIMARY KEY,
       name TEXT,
       email TEXT)
    """
)

@app.get("/customers")
def get_customers():
    cursor.execute("SELECT * FROM customer")
    customers = cursor.fetchall()
    return customers

@app.post("/customers")
def create_customer(customer: Customer):
    cursor.execute(
        "INSERT INTO customer(name, email) VALUES (?, ?)",
        (customer.name, customer.email)
    )
    connection.commit()
    return customer

@app.put("/customers/{id}")
def update_customer(id: int, customer: Customer):
    cursor.execute(
        "UPDATE customer SET name = ?, email = ? WHERE id = ?",
        (customer.name, customer.email, id)
    )
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Customer not found")
    connection.commit()
    return customer

@app.delete("/customers/{id}")
def delete_customer(id: int):
    cursor.execute(
        "DELETE FROM customer WHERE id = ?",
        (id,)
    )
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Customer not found")
    connection.commit()
    return {"message": "Customer deleted"}