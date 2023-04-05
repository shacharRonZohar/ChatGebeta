import logging
from flask import Flask, request, jsonify
from dotenv import load_dotenv

from .services.gpt import query
from .services.logger import logger

from .schemas.chat import ChatInputSchema
# from .services.util import log

logging.basicConfig(level=logging.DEBUG)
load_dotenv()


app = Flask(__name__)


@app.get('/api')
def welcome():
    return {'data': 'Welcome to ChatGebeta, a ChatGPT api wrapper'}


@app.post('/api/chat')
def chat():
    logger.info('Request made to /chat, validating input')
    user_input = validate_input(request)
    print(user_input)
    # The validate_input function returns a dictionary if the input is invalid
    if "error" in user_input:
        logger.info('Input validation failed, returning error')
        return user_input, 400
    logger.info('Input validated, querying the model')
    try:
        response = query(user_input)
        return {'data': response}

    except Exception as e:
        # I wanted to log the error for internal use, while returning a user friendly error message
        internal_msg = f"Had an error while querying the model, type: {type(e).__name__}, {e.args}"
        logger.exception(internal_msg)
        user_msg = 'Something went wrong while querying the model, please try again'
        return {'error': user_msg}, 500


def validate_input(request):
    if not request.is_json:
        return {'error': 'Request must be a JSON request'}

    input_data = request.get_json()
    errors = ChatInputSchema().validate(input_data)
    if errors:
        return {'error': errors}

    return input_data
