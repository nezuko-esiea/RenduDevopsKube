import os

def test_files_exist():
    """Vérifie que les fichiers essentiels sont présents dans le dossier"""
  
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    
    assert os.path.exists(os.path.join(parent_dir, "api.py"))
    assert os.path.exists(os.path.join(parent_dir, "requirements.txt"))
    assert os.path.exists(os.path.join(parent_dir, "Dockerfile"))