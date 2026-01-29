from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_employee():
    response = client.post("/employees", json={
        "name": "Raman",
        "address": "Guntur",
        "salary": 40000,
        "age": 24
    })
    assert response.status_code == 200
