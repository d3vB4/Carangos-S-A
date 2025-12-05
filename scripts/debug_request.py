import requests
from app import app

def test_render():
    client = app.test_client()
    
    # Login as admin
    client.post('/login', data={'username': 'admin', 'password': 'admin123'})
    
    print("Testing GET /operacional...")
    try:
        response = client.get('/operacional')
        if response.status_code == 200:
            print("GET Success")
            print(response.data.decode('utf-8'))
        else:
            print(f"GET Failed: {response.status_code}")
            print(response.data.decode('utf-8'))
    except Exception as e:
        print(f"GET Exception: {e}")

    print("Testing POST /operacional...")
    try:
        response = client.post('/operacional', data={
            'dia': 'Segunda',
            'turno': 'Manhã',
            'quantidade': 10
        }, follow_redirects=True)
        if response.status_code == 200:
            print("POST Success")
        else:
            print(f"POST Failed: {response.status_code}")
            print(response.data.decode('utf-8'))
    except Exception as e:
        print(f"POST Exception: {e}")

if __name__ == "__main__":
    test_render()
