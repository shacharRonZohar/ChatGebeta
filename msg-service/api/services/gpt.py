from os import environ
from requests import post

API_URL = 'http://localhost:5050/api/model/'

headers = {'Authorization': f"Bearer {environ['API_TOKEN']}"}


def query(payload):
    endpoint = 'generate/'
    url = f'{API_URL}{endpoint}'
    # The api returns a list with a single dictionary, containing the generated text
    response = post(url, headers=headers, json=payload).json()
    data = response[0]['generated_text']
    return {'user_input': payload, 'bot_response': data}
