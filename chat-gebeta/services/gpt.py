from os import environ
from requests import post

# See https://huggingface.co/inference-api for more information
API_URL = 'https://api-inference.huggingface.co/models/gpt2'

headers = {'Authorization': f"Bearer {environ['API_TOKEN']}"}


def query(payload):
    print(payload)
    # The api returns a list with a single dictionary, containing the generated text
    response = post(API_URL, headers=headers, json=payload).json()
    print(response)
    data = response[0]['generated_text']
    return {'user_input': payload, 'bot_response': data}
