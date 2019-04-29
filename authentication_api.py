from flask import Flask, request, jsonify

app = Flask(__name__)

TOKEN = 'abcde12345'

@app.route('/authentication/token', methods=['POST'])
def authenticate():
    print(request)
    values = request.get_json(force = True)
    print('받은 값', values)

    if 'token' not in values:
        return 'Missing values', 400

    token = values['token']
    if token == TOKEN:
        response = {'message': f'You are authenticated. {token} / {TOKEN}'}
    else:
        response = {'message': 'Denied'}

    return jsonify(response), 201
