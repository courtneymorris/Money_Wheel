import random
from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/', methods=["GET"])
def add_profile():
   return "Hello world" # HTML file to go here



prize_wheel = {
    '0': 6,
    '1': 5,
    '$5': 4,
    '$25': 3,
    '$100': 2,
    '$500': 1
}

def money_wheel(prizes):
    segments = []

    for prize, chance in prizes.items():
        for _ in range(chance):
            segments.append(prize)

    return random.choice(segments)






if __name__ == '__main__':
    app.run(debug=True)