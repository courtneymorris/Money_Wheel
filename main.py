import random

spin_cost = 5
my_wallet = 15
winnings = 0
wheel = {
    0 : 6,
    1: 5,
    5 : 4,
    25 : 3,
    100 : 2,
    500 : 1
}


def hasFunds():
     return my_wallet > spin_cost


def gamble():
    if not hasFunds():
          print(f'Not enough funds, your wallet balance is ${wallet}')
          return
    else:
        segments = []
        for prize, chance in wheel.items():
            for _ in range(chance):
                segments.append(prize)
                winnings = random.choice(segments)
                wallet = my_wallet + (winnings  - spin_cost)

        if winnings > 0:
            print(f'Congratulations! You\'ve won ${winnings}! You have ${wallet} left. Let\'s play again!')
        else:
            print(f'Oof, bad luck! Want to spin again? Current balance is ${wallet}')

hasFunds()
gamble()