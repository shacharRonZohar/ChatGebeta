from ChatGebetaMsg.models import db, Chat, ChatMsg


def get_chat_by_id(id):
    return Chat.query.filter_by(id=id).first()


def get_chat_by_user_id(user_id):
    return Chat.query.filter_by(user_id=user_id).all()


def save_new_chat(response, chat_id=None):
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
