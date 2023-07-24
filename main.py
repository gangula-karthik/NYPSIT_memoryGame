from flask import Flask, request, render_template, jsonify
import csv
import json
import random
from supabase import create_client, Client
from flask import Flask, request
import os

app = Flask(__name__)

# Initialize Supabase client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)



@app.route('/')
def home():
    leaderboard = supabase.table('Leaderboard').select().order('score').execute()
    res = leaderboard['data']
    return render_template('index.html', leaderboard=res)





@app.route('/game', methods=['GET', 'POST'])
def myGame():
    with open('cards.json') as f:
        cards = json.load(f)
    random.shuffle(cards)
    return render_template('memoryCards.html', cards=cards)


@app.route('/record-time', methods=['POST'])
def save():
    data = request.get_json()
    if int(data["score"]) > 0: 
        # Insert data into Supabase
        insert_data = {
            "name": data['name'],
            "adminNumber": data['adminNumber'],
            "score": int(data['score'])
        }
        supabase.table("Leaderboard").insert(insert_data)

    return '', 204



# @app.route('/record-time', methods=['POST'])
# def record_time():
#     data = request.get_json()
#     time_taken = data['timeTaken']

#     # with shelve.open('leaderboard') as db:
#     #     for key in db:
#     #         if key == data['adminNo']:
#     #             db[key]['time'] = time_taken

#     return {'message': 'Time recorded successfully'}


if __name__ == '__main__':
    app.run(debug=True)
