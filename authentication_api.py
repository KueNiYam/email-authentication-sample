from flask import Flask, request, jsonify

app = Flask(__name__)

TOKEN = 'abcde12345'

@app.route('/authentication/token', methods=['POST'])
def authenticate():
    if 'token' not in request.form:
        return 'Missing values', 400

    token = request.form['token']

    if token == TOKEN:
        response = {'message': f'You are authenticated. {token} / {TOKEN}'}
        return jsonify(response), 201
    else:
        response = {'message': 'Denied'}
        return jsonify(response), 200
