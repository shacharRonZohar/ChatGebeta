import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    chats = db.relationship('Chat', backref='user', lazy=True)

    def __repr__(self):
        return f'User {self.username}'

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    msgs = db.relationship('ChatMsg', backref='chat', lazy=True)

    # def __repr__(self):
    #     return f'Chat {self.id}'

    # def __init__(self, user_id):
    #     self.user_id = user_id


class ChatMsg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False)
    user_input = db.Column(db.String(1024), nullable=False)
    bot_response = db.Column(db.String(1024), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    # def __repr__(self):
    #     return f'Msg {self.id}, {self.user_input}, {self.bot_response}'

    # def __init__(self, chat_id, user_input, bot_response):
    #     self.chat_id = chat_id
    #     self.user_input = user_input
    #     self.bot_response = bot_response
