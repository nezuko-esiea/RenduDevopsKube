# import pytest
# from api import create_app

# @pytest.fixture
# def client():
#     app = create_app()
#     with app.test_client() as client:
#         yield client

# def test_health(client):
#     """Vérifie que l'API répond bien"""
#     rv = client.get('/health')
#     assert rv.status_code == 200