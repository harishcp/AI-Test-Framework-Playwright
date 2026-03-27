import requests

def test_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200