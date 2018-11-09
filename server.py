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
    return jsonify(data)
 
@app.route('/', methods=['POST'])
def root_post():
    print(request.form)
    return "OKAY" 

@app.route('/vote',methods=['GET'])
def vote():
    with open('index.html') as f:
        return f.read()

if __name__ == '__main__':
    app.run('0.0.0.0',port=os.environ['PORT'],debug=True)