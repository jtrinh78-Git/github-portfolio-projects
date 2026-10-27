from fastapi import FastAPI
from pydantic import BaseModel

class Customer(BaseModel):
     name: str
     email: str

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/hello")
def hello():
    return {"message": "Hello Joe"}

@app.get("/hello/{name}")
def hello_name(name: str):
    return {"message": f"Hello {name}"}

@app.get("/search")
def search(name: str):
    return {"search_result": name}

@app.post("/customers")
def create_customer(customer: Customer):
        return {"name": customer.name, "email": customer.email}

@app.get("/customers")
def get_customers():
     return {"customers": ["Joseph", "Sarah", "Bob"]}

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
     return {"message": f"Customer {customer_id} deleted"}

@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, customer: Customer):
    return {"customer_id": customer_id, "name": customer.name, "email": customer.email}


