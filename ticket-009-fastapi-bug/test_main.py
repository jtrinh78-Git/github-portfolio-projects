from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_existing_customer():
    response = client.get("/customers/2")
    assert response.status_code == 200
    assert response.json()["customer"]["name"] == "Sarah"


def test_get_missing_customer():
    response = client.get("/customers/99")
    assert response.status_code == 404
    assert response.json()["detail"] == "Customer not found"