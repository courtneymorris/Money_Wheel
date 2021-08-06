import random


prize_wheel = {
    '0': 12,
    '$5': 6,
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


# print(money_wheel(prize_wheel))