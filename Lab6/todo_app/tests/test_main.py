# tests/test_main.py

from fastapi.testclient import TestClient
import sys
sys.path.append("..")
from main import app


client = TestClient(app)

def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200

def test_create_book():
    response = client.post("/books/", json={"title": "Sample Book", "author": "Sample Author"})
    assert response.status_code == 200
