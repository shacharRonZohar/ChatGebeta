import logging
from flask import Flask, request
from dotenv import load_dotenv

from .services.gpt import query
from .services.logger import logger

from .schemas.chat import ChatInputSchema
# from .services.util import log

logging.basicConfig(level=logging.DEBUG)
load_dotenv()


app = Flask(__name__)

@app.post('/api/model/generate')
def generate():
    input_data = validate_input(request)

    if isinstance(input_data, dict):
        return input_data, 400

    response = query(input_data)
    return response


def validate_input(request):
    if not request.is_json:
        return {'error': 'Request must be a JSON request'}

    input_data = request.get_json()
    errors = ChatInputSchema().validate(input_data)
    if errors:
        return {'error': errors}

    return input_data["message"]
