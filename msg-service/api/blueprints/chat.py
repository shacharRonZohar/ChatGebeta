from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from ..services.gpt import query
from ..services.logger import logger

from ..schemas.validation.main import validate_chat_input

bp = Blueprint('api', __name__)


@bp.get('/')
def index():
    return {'data': 'Welcome to ChatGebeta, a ChatGPT api wrapper'}


@bp.post('/chat')
def chat():
    logger.info('Request made to /chat, validating input')
    user_input = validate_chat_input(request)
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
