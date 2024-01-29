import pytest
import {{cookiecutter.repo_name}}
from fastapi import testclient
from {{cookiecutter.repo_name}}.app import init_app
from {{cookiecutter.repo_name}}.controllers.operations import health_check


@pytest.fixture(scope="module")
def app():
    return init_app(False)


@pytest.fixture(scope="function")
def client(app):
    return testclient.TestClient(app)


def test_healthcheck(client: testclient.TestClient) -> None:
    response = client.get("/api/ops/health_check/")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_healthcheck_version(client: testclient.TestClient) -> None:
    response = client.get("/api/ops/health_check/")
    payload = response.json()
    assert isinstance(payload, dict)
    assert payload["version"] == {{cookiecutter.repo_name}}.__version__
