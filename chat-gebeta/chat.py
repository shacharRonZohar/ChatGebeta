from flask import Flask, request, jsonify
from dotenv import load_dotenv

from .services.util import log
from .services.gpt import query
load_dotenv()


app = Flask(__name__)


@app.get('/')
def welcome():
    return {'data': 'Welcome to ChatGebeta, a ChatGPT api wrapper'}


@app.post('/chat')
def chat():
    log('Request made to /chat, validating input')
    input = validate_input(request)
    # The validate_input function returns a dictionary if the input is invalid
    if type(input) == dict:
        log('Input validation failed, returning error')
        return input, 400
    log('Input validated, querying the api')
    try:
        response = query(input)
        return {'data': response}

    except Exception as e:
        # I wanted to log the error for internal use, while returning a user friendly error message
        internal_msg = f"Had an error while querying the api, type: {type(e).__name__}, {e.args}"
        log(internal_msg)
        user_msg = 'Something went wrong while querying the api, please try again'
        return {'error': user_msg}, 500


def validate_input(request):
    if not request.is_json:
        return {'error': 'Request must be a JSON request'}
    message = request.get_json().get('message')
    if not message:
        return {'error': 'Please provide a message'}
    if type(message) != str:
        return {'error': 'Message must be a string'}
    if len(message) > 1024:
        return {'error': 'Message is too long'}

    return message
