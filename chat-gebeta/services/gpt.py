from os import environ
from requests import post

# See https://huggingface.co/inference-api for more information
API_URL = 'https://api-inference.huggingface.co/models/gpt2'

headers = {'Authorization': f"Bearer {environ['API_TOKEN']}"}


def query(payload):
    # The api returns a list with a single dictionary, containing the generated text
    response = post(API_URL, headers=headers, json=payload).json()
    raw_data = response[0]['generated_text']
    # The generated text contains both the input and the output, so we need to split it
    split_string = f"{payload}\n\n"
    data = raw_data.split(split_string)[1]
    return {'user_input': payload, 'bot_response': data}
