import requests


def fetch_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {}