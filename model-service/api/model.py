import logging

# from dotenv import load_dotenv
from flask import (
    Blueprint, request
)

from .schemas.validation.main import validate_generation_input
from .services.gpt import query

bp = Blueprint('model', __name__)


@bp.post('/generate')
def generate():
    input_data = validate_generation_input(request)
    if "error" in input_data:
        logging.info(f"Input validation failed, returning error: {input_data}")
        return input_data, 400

    logging.info(f"Input validated, querying the model with: {input_data}")
    try:
        max_response_length = input_data.get("max_response_length", None)
        response = query(
            message=input_data["message"], max_response_length=max_response_length)
        return response
    except Exception as e:
        # I wanted to log the error for internal use, while returning a user friendly error message
        internal_msg = f"Had an error while querying the model, type: {type(e).__name__}, {e.args}"
        logging.exception(internal_msg)
        user_msg = 'Something went wrong while querying the model, please try again'
        return {'error': user_msg}, 500
