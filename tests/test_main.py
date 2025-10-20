import uuid

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_get_items_empty():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item():
    response = client.post("/items?name=test_item")
    assert response.status_code == 200
    item_id = response.json()
    assert uuid.UUID(item_id)


def test_get_item():
    response = client.post("/items?name=test_item_2")
    item_id = response.json()

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == "test_item_2"


def test_get_items_non_empty():
    client.post("/items?name=item1")
    client.post("/items?name=item2")

    response = client.get("/items")
    assert response.status_code == 200
    items = response.json()
    assert len(items) >= 2


def test_get_item_not_found():
    random_id = str(uuid.uuid4())
    response = client.get(f"/items/{random_id}")
    assert response.status_code == 200
    assert response.json() is None


def test_fib_endpoint():
    response = client.get("/fib/5")
    assert response.status_code == 200
    assert response.json() == 8

    response = client.get("/fib/10")
    assert response.status_code == 200
    assert response.json() == 89
