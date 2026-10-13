# Section 1
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Section 2

customers = {
    1: {"name": "David", "balance": 100},
    2: {"name": "Sarah", "balance": 200},
    3: {"name": "Michael", "balance": 300}
}

# Section 3
@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    customer = customers.get(customer_id)
    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    return {"customer": customer}