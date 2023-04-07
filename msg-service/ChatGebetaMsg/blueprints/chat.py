import logging

# from ChatGebetaMsg.models import db, Chat, ChatMsg
from ChatGebetaMsg.services.db import save_new_chat, get_chat_by_id, get_chat_by_user_id
from ChatGebetaMsg.services.gpt import query
from ChatGebetaMsg.validation.main import validate_chat_input
from flask import (
    Blueprint, g, redirect, render_template, request, url_for
)

from .auth import login_required

bp = Blueprint('chat', __name__)


@bp.get('/')
def index(msgs=None):
    return render_template('chat/index.html', msgs=msgs)


@login_required
@bp.get('/<string:id>')
def index_with_history(id):
    try:
        return index(msgs=get_msgs(id=id))
    except AttributeError:
        return redirect(url_for('chat.index'))


@login_required
@bp.get('/history')
def chat_history():
    chats = get_chat_by_user_id(user_id=g.user.id)
    return render_template('chat/chat-history.html', chats=chats)


@bp.get('/api')
def api_index():
    return {'msg': 'Welcome to ChatGebeta, a ChatGPT api wrapper'}


@bp.post('/api/generate')
def chat(chat_id=None):
    logging.getLogger().info('Request made to /chat, validating input')
    user_input = validate_chat_input(request)
    # The validate_input function returns a dictionary if the input is invalid
    if "error" in user_input:
        logging.info('Input validation failed, returning error')
        return user_input, 400
    logging.info('Input validated, querying the model')
    try:
        message = user_input['message']

        response = query({
            'message': message,
        })
        if g.user is not None:
            save_new_chat(response=response, chat_id=chat_id)
        return response
    except Exception as e:
        # I wanted to log the error for internal use, while returning a user friendly error message
        internal_msg = f"Had an error while querying the model, type: {type(e).__name__}, {e.args}"
        logging.exception(internal_msg)
        user_msg = 'Something went wrong while querying the model, please try again'
        return {'error': user_msg}, 500


@login_required
@bp.post('/<string:id>/api/generate')
def chat_with_history(id):
    return chat(chat_id=id)


@login_required
@bp.get('/api/history')
def get_chats():
    return get_chat_by_user_id(user_id=g.user.id)


@login_required
@bp.get('/<string:id>/api/msgs')
def get_msgs(id):
    chat = get_chat_by_id(id=id, user_id=g.user.id)
    if chat is None:
        return redirect(url_for('chat.index'))
    print(chat.msgs)
    return chat.msgs
