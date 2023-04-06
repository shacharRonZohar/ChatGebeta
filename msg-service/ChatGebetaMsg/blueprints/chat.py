import logging

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


from ..schemas.validation.main import validate_chat_input

from .auth import login_required
from ..db import get_db

from ..services.gpt import query

bp = Blueprint('api', __name__)


@bp.get('/')
def index():
    return render_template('chat/index.html')


@bp.get('/<string:id>')
def index_with_history(id):
    db = get_db()
    history = db.execute(
        'SELECT FROM chat WHERE id = ?', (id,)
    ).fetchall()
    return render_template('chat/index.html', )


@bp.get('/chat-history')
@login_required
def chat_history():
    return render_template('chat/chat-history.html')


@bp.get('/api')
def api_index():
    return {'data': 'Welcome to ChatGebeta, a ChatGPT api wrapper'}


@bp.post('/api/generate')
def chat():
    logging.info('Request made to /chat, validating input')
    user_input = validate_chat_input(request)
    # The validate_input function returns a dictionary if the input is invalid
    if "error" in user_input:
        logging.info('Input validation failed, returning error')
        return user_input, 400
    logging.info('Input validated, querying the model')
    try:
        print(user_input)
        response = query(user_input)
        return {'data': response}
    except Exception as e:
        # I wanted to log the error for internal use, while returning a user friendly error message
        internal_msg = f"Had an error while querying the model, type: {type(e).__name__}, {e.args}"
        logging.exception(internal_msg)
        user_msg = 'Something went wrong while querying the model, please try again'
        return {'error': user_msg}, 500