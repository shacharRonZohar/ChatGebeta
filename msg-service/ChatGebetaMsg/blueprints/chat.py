import logging

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from ChatGebetaMsg.validation.main import validate_chat_input

from .auth import login_required
from ChatGebetaMsg.models import db, Chat, ChatMsg
from ChatGebetaMsg.services.gpt import query

bp = Blueprint('chat', __name__)


@bp.get('/')
def index(msgs=None):
    return render_template('chat/index.html', msgs=msgs)


@bp.get('/<string:id>')
@login_required
def index_with_history(id):
    try:
        msgs = Chat.query.filter_by(id=id).first().msgs
        return index(msgs=msgs)
    except AttributeError:
        return redirect(url_for('chat.index'))


@bp.get('/history')
@login_required
def chat_history():
    chats = Chat.query.filter_by(user_id=g.user.id).all()
    return render_template('chat/chat-history.html', chats=chats)


@bp.get('/api')
def api_index():
    return {'msg': 'Welcome to ChatGebeta, a ChatGPT api wrapper'}


@bp.post('/<string:id>/api/generate')
def chat_with_history(id):
    return chat(chat_id=id)


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
        if 'user' in g:
            _save_new_chat(response=response, chat_id=chat_id)
        return response
    except Exception as e:
        # I wanted to log the error for internal use, while returning a user friendly error message
        internal_msg = f"Had an error while querying the model, type: {type(e).__name__}, {e.args}"
        logging.exception(internal_msg)
        user_msg = 'Something went wrong while querying the model, please try again'
        return {'error': user_msg}, 500


def _save_new_chat(response, chat_id=None):
    _add_chat(response) if chat_id is None else _add_chat_msg(
        response, chat_id)


def _add_chat(response):
    new_chat = Chat(user_id=g.user.id)
    db.session.add(new_chat)
    db.session.commit()
    _add_chat_msg(response, new_chat.id)


def _add_chat_msg(response, chat_id):
    new_msg = ChatMsg(
        chat_id=chat_id, user_input=response['user_input'], bot_response=response['bot_response'])
    db.session.add(new_msg)
    db.session.commit()
