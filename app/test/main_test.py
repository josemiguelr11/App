from fastapi.testclient import TestClient
from routes.route_user import app_user

client = TestClient(app_user)


def test_read_main():
    response = client.get("/users")
    assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}