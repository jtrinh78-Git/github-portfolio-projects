# =====================================
# SECTION 1 — IMPORTS AND TEST CLIENT
# =====================================

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# SECTION 2 - TEST EXISTING
def test_get_existing_customer():
    response = client.get("/customers/2")

    assert response.status_code == 200
    assert response.json()["id"] == 2
    assert response.json()["name"] == "Bob"

# SECTION 3 - TEST MISSING CUSTOMER

def test_get_missing_customer():
    response = client.get("/customers/0")

    assert response.status_code == 404
    assert response.json()["detail"] == "Customer not found"