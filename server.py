from flask import Flask, app, request,jsonify
from flask_cors import CORS
from random import randint
import pandas as pd
import chardet
from filter import replace_string

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
    return "OK" 

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)