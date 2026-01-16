import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from api import create_app 

@pytest.fixture
def client():
    app = create_app()
    return app.test_client()

def test_health_check(client):
    """Vérifie que l'API répond bien sur le endpoint /health"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}