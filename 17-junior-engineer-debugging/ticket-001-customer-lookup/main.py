# =====================================
# SECTION 1 — IMPORTS
# =====================================

import sqlite3
from fastapi import FastAPI, HTTPException

# =====================================
# SECTION 2 — APPLICATION
# =====================================

app = FastAPI()

DATABASE = "customers.db"

# =====================================
# SECTION 3 — DATABASE SETUP
# =====================================

def setup_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM customers")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany(
            "INSERT INTO customers (id, name, email) VALUES (?, ?, ?)",
            [
                (1, "Alice", "alice@example.com"),
                (2, "Bob", "bob@example.com"),
                (3, "Charlie", "charlie@example.com"),
            ],
        )

    conn.commit()
    conn.close()


setup_database()

# =====================================
# SECTION 4 — CUSTOMER LOOKUP
# =====================================

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, email FROM customers WHERE id = ?",
        (customer_id,),
    )

    customer = cursor.fetchone()
    conn.close()

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )

    return {
        "id": customer[0],
        "name": customer[1],
        "email": customer[2],
    }