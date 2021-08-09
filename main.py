import random
from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/', methods=["GET"])
def add_profile():
   return "Hello world" # HTML file to go here





money_wheel = {
    0 : 6,
    1: 5,
    5 : 4,
    25 : 3,
    100 : 2,
    500 : 1
}

my_wallet = 15

def spin(wheel, wallet):
    segments = []
    
    for prize, chance in wheel.items():
        for _ in range(chance):
            segments.append(prize)
            prize_won = random.choice(segments)
    wallet = wallet + (prize_won - 5)

    if prize_won != 0:
        print(f'Congratulations! You\'ve won ${prize_won}! You have ${wallet} left. Let\'s play again!')
    else:
        print(f'Oof, bad luck! Want to spin again?')

    return wallet


my_wallet = spin(money_wheel, my_wallet)
my_wallet = spin(money_wheel, my_wallet)
my_wallet = spin(money_wheel, my_wallet)
my_wallet = spin(money_wheel, my_wallet)
my_wallet = spin(money_wheel, my_wallet)
my_wallet = spin(money_wheel, my_wallet)






if __name__ == '__main__':
    app.run(debug=True)