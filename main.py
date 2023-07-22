from flask import Flask, request, render_template, jsonify
import csv
import json
import random
import shelve

app = Flask(__name__)

name = None

@app.route('/')
def home():
    with open('Leaderboard.csv') as f:
        reader = csv.reader(f)
        res = []
        for i in list(reader): 
            res.append(i)
            res[-1][-1] = int(res[-1][-1])
        res = sorted(res, key=lambda x: x[-1], reverse=False)
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
        with open('Leaderboard.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([data['name'], data['adminNumber'], int(data['score'])])

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
