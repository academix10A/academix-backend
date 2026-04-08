from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "active"

def test_api_docs():
    response = client.get("/docs")
    assert response.status_code == 200