from os import environ
from requests import post

API_URL = 'http://localhost:5050/api/model/'

# headers = {'Authorization': f"Bearer {environ['API_TOKEN']}"}


def query(payload):
    endpoint = 'generate/'
    url = f'{API_URL}{endpoint}'
    return post(url, json=payload).json()
