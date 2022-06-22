from fastapi.testclient import TestClient
from src.models.user import CreateUserRequest


create_user = dict(CreateUserRequest(name="Name Test", r="Register Test", password="password_test"))


def test_create_factory(client: TestClient):
    response = client.post("/v1/users/create", json=create_user)

    expected_response = 201
    assert response.status_code == expected_response
