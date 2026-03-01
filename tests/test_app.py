import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app import app  # Fixed import!

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Flask' in rv.data

def test_health(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert b'OK' in rv.data
