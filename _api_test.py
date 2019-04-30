import requests

url = 'http://127.0.0.1:5000/authentication/token'

data = {'token': 'abcde12345'}

req = requests.post(url, json=data)
    # "{'token': 'abcde12345'}" 전송
req = requests.post(url, data=data)
    # "'token'='abcde12345'" 전송
