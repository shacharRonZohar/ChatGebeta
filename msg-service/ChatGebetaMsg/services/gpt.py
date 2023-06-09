from requests import post

# For local self hosted model
# API_URL = 'http://localhost:5050/api/model/'
# For self hosted model
API_URL = 'https://chatgebeta-model-production.up.railway.app/api/model/'


def query(payload):
    endpoint = 'generate'
    url = f'{API_URL}{endpoint}'
    return post(url, json=payload).json()
