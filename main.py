from flask import Flask, request, render_template
import csv
import json
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/game')
def game():
    with open('cards.json') as f:
        cards = json.load(f)
    random.shuffle(cards)  # This shuffles the list of cards in-place
    return render_template('memoryCards.html', cards=cards)


@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()

    with open('leaderboard.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([data['name'], data['adminNo'], data['time']])

    return '', 204  # No content

if __name__ == '__main__':
    app.run(debug=True)
