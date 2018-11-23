from flask import Flask, app, request,jsonify
from flask_cors import CORS
from random import randint
import pandas as pd
from filter import replace_string
import os
import psycopg2
import csv
from sqlalchemy import create_engine

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur=conn.cursor()
#engine = create_engine(DATABASE_URL)

app = Flask(__name__)
CORS(app)

tweet_data = pd.read_csv('tweets.csv')

@app.route('/', methods=['GET'])
def root():
    '''tweet = tweet_data.sample(1).iloc[0]
    text = tweet.text
    data = {
        'id':tweet.id,
        'text':text,
        'created_at':tweet.created_at
    }
    return jsonify(data)'''
    #The code above is used for df 

    #The code below is for psql
    cur.execute('SELECT * FROM tweet_table ORDER BY random() LIMIT 1;')
    try:
        query_result = cur.fetchone()
    except:
        query_result = [1,'Server error', '11-01-1998']
    data = {
        'id':query_result[0],
        'text':query_result[1],
        'created_at':query_result[2]
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

@app.route("/vote",methods=['POST'])
def post_vote():
    id = request.form.get('id',1)
    column = 'fake_count' if request.form.get('response','fake') == 'fake' else 'real_count'
    cur.execute(f"UPDATE tweet_table SET {column} = {column} + 1 where id={id}")
    conn.commit()
    return "OK"

@app.route("/load_csv", methods=['POST'])
def load_csv():
    f = request.files['data']
    df = pd.read_csv(f)
    for index, row in df.iterrows():
        cur.execute(f"SELECT COUNT(1) FROM tweet_table WHERE id = {row['id']};")
        query_result = cur.fetchone()[0]
        if query_result < 1:
            try:
                id=row['id']
                text=row['text']
                created_at=row['created_at']
                cur.execute(f"INSERT INTO tweet_table VALUES ({id},'{text}', '{created_at}',0,0)")
            except:
                print("Tweet with id already exists")
            #{row["id"]},{row["text"},{row["created_at"]},{0},{0}
        else:
            print("Found duplicated id, not adding it up")
    conn.commit()
    return "File Loaded"

@app.route("/report", methods=["GET"])
def generate_report():
    cur.execute("SELECT * FROM tweet_table")
    r = cur.fetchall()
    data = {}
    for e in r:
        data[e[0]] = {
            'text' : e[1],
            'created_at': e[2],
            'fake_count': e[3],
            "real_count": e[4]
        }
    return jsonify(data)

if __name__ == '__main__':
    app.run('0.0.0.0',port=os.environ['PORT'],debug=True)

