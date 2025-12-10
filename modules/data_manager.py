import json
import os

# Allow custom data directory via environment variable (useful for cloud deployments)
DATA_DIR = os.getenv('DATA_DIR', os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data'))

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def load_data(filename):
    """
    Loads data from a JSON file.
    Returns an empty list if file doesn't exist or is invalid.
    """
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        return []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_data(filename, data):
    """
    Saves data to a JSON file.
    """
    filepath = os.path.join(DATA_DIR, filename)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Erro ao salvar {filename}: {e}")
        return False
