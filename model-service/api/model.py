import logging

# from dotenv import load_dotenv
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from .services.gpt import query

from .schemas.chat import ChatInputSchema


bp = Blueprint('model', __name__)


@bp.post('/generate')
def generate():
    input_data = validate_input(request)
    if isinstance(input_data, dict):
        logging.info(f"Input validation failed, returning error: {input_data}")
        return input_data, 400

    logging.info(f"Input validated, querying the model with: {input_data}")
    try:
        response = query(input_data)
        return response
    except Exception as e:
        # I wanted to log the error for internal use, while returning a user friendly error message
        internal_msg = f"Had an error while querying the model, type: {type(e).__name__}, {e.args}"
        logging.exception(internal_msg)
        user_msg = 'Something went wrong while querying the model, please try again'
        return {'error': user_msg}, 500


def validate_input(request):
    if not request.is_json:
        return {'error': 'Request must be a JSON request'}

    input_data = request.get_json()
    errors = ChatInputSchema().validate(input_data)
    if errors:
        return {'error': errors}

    return input_data["message"]
