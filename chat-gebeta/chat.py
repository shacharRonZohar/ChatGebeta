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
    input = validate_input(request)
    if type(input) == dict:
        return input, 400

    try:
        response = query(input)
        return jsonify({'data': response})
    except Exception as e:
        internal_msg = f"Had an error while querying the api, type: {type(e).__name__}, {e.args}"
        user_msg = 'Something went wrong while querying the api, please try again'
        print(internal_msg)
        return jsonify({'error': user_msg}), 500
    # try:
    #     message = request.json['message']
    # except KeyError:
    #     return {'error': 'Please provide a message'}, 400
    # try:
    #     validate_input(message)
    # except ValueError as e:
    #     return {'error': e.args[0]}, 400
    # try:
    #     return {'data': query(message)}
    # except Exception as e:
    #     internal_msg = f"Had an error while querying the api, type: {type(e).__name__}, {e.args}"
    #     user_msg = 'Something went wrong while querying the api, please try again'
    #     print(internal_msg)
    #     return {'error': user_msg}, 500


def validate_input(request):
    if not request.is_json:
        return {'error': 'Request must be a JSON request'}
    message = request.get_json().get('message')
    if not message:
        return {'error': 'Please provide a message'}
    if type(message) != str:
        return {'error': 'Message must be a string'}
    if len(message) > 1024:
        return {'error': 'Message is too long'}

    return message
