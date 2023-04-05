from .services.gpt import query
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)


@app.get('/')
def welcome():
    return {'data': 'Welcome to ChatGebeta, a ChatGPT api wrapper'}


@app.post('/chat')
def chat():
    message = request.json['message']
    return {'data': query(message)}
