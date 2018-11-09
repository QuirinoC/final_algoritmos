from flask import Flask, app, request,jsonify
from flask_cors import CORS
from random import randint
import pandas as pd
from filter import replace_string
import os

app = Flask(__name__)
CORS(app)

tweet_data = pd.read_csv('tweets.csv')

@app.route('/', methods=['GET'])
def root():
    tweet = tweet_data.sample(1).iloc[0]
    text = tweet.text
    data = {
        'id':tweet.id,
        'text':text,
        'created_at':tweet.created_at
    }
    return f'''<!DOCTYPE html>\n<html>\n\n<head>\n    <meta charset="utf-8" />\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <title>Page Title</title>\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <script src="https://code.jquery.com/jquery-3.3.1.js" integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60="\n      crossorigin="anonymous"></script>\n    <script src="{{url_for('static', filename='main.js')}}"></script>\n</head>\n \n<body>\n    <center>\n        <h1>Fake or not</h1>\n        <p      id="tweet">{data['text']}</p>\n        <button id="fake">Fake</button>\n        <button id="real">Real</button>\n    </center>\n\n</body>\n\n</html>'''

@app.route('/', methods=['POST'])
def root_post():
    print(request.form)
    return "OKAY" 

if __name__ == '__main__':
    app.run('0.0.0.0',port=os.environ['PORT'],debug=True)