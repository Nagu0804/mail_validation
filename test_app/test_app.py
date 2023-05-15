import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_valid_email(client):
    data = {'email': 'example@example.com'}
    response = client.post('/validate_email', data=data)
    assert response.status_code == 200
    assert b'Email is valid' in response.data

def test_invalid_email(client):
    data = {'email': 'example'}
    response = client.post('/validate_email', data=data)
    assert response.status_code == 200
    assert b'Email is not validate' in response.data


