from flask import Flask, request, render_template, jsonify
import csv
import json
import random
import shelve

app = Flask(__name__)

name = None

db = shelve.open('leaderboard', writeback=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-leaderboard', methods=['GET'])
def get_leaderboard():
    with shelve.open('leaderboard') as db:
        leaderboard = [value for value in db.values()]

    return jsonify(leaderboard)



@app.route('/game')
def myGame():
    with open('cards.json') as f:
        cards = json.load(f)
    random.shuffle(cards)  # This shuffles the list of cards in-place
    return render_template('memoryCards.html', cards=cards)


@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()

    with shelve.open('leaderboard'  ) as db:
        db[data['adminNo']] = {'name': data['name'], 'adminNo': data['adminNo']}

    return '', 204  # No content

@app.route('/record-time', methods=['POST'])
def record_time():
    data = request.get_json()
    time_taken = data['timeTaken']

    with shelve.open('leaderboard') as db:
        for key in db:
            if key == data['adminNo']:
                db[key]['time'] = time_taken

    return {'message': 'Time recorded successfully'}


if __name__ == '__main__':
    app.run(debug=True)
