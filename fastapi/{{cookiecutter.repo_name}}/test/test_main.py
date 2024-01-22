from fastapi.testclient import TestClient
from {{cookiecutter.repo_name}}.main import app


def test_health_check():
    client = TestClient(app)
    response = client.get("/health_check")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "OK"
