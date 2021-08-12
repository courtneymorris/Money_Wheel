import random
import time



spin_cost = 5
winnings = 0
wheel = {
    0 : 20,
    1: 15,
    5 : 10,
    25 : 5,
    50 : 2,
    500 : 1
}


def hasFunds(wallet):
    if wallet >= spin_cost:
        return True


def gamble(wallet):

    segments = []
    for prize, chance in wheel.items():
        for _ in range(chance):
            segments.append(prize)

    winnings = random.choice(segments)
    
    wallet = wallet + winnings - spin_cost

    if winnings > 0 and winnings < 500 and wallet >= 5:
        print(f'\n\nCONGRATULATIONS!!! \n\nYou\'ve WON ${winnings}! \n\nYou have ${wallet} left.')
    elif winnings > 0 and wallet < 5:
        print(f'YAY! You won ${winnings}!\n\n')
        time.sleep(1)
        print(". . .\n\n")
        time.sleep(1)
        print(f'. . .but you only have ${wallet}, which isn\'t enough to play again.')
    elif winnings == 500:
        print("JACKPOT!!!!!!!\n\n")
        time.sleep(.5)
        print("You've won $500!!!!!")
    elif winnings == 0 and hasFunds(wallet):
        print(f'\n\nOOF, bad luck!\n\nYou didn\'t win this time.\n\nYou have ${wallet} left')
    
    return wallet




print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWELCOME")
time.sleep(.5)
print("\nTO")
time.sleep(.5)
print("\nTHE")
time.sleep(.5)
print("\nCASINO")
time.sleep(2)
my_wallet = int(input("\n\n\nHow much did you bring to gamble today?\n\n$"))
print("\n\n\nWOW, big spender!")
time.sleep(.5)
print("\nIt's just $5 to spin the wheel!")
time.sleep(.5)
start_response = input("\nReady to spin?\n\n")


def play(wallet):

    print("\n\n\n\nSPINNING")
    time.sleep(.5)
    print("\nSPINNING")
    time.sleep(.5)
    print("\nSPINNING")
    time.sleep(.5)
    print("\nSPINNING")
    time.sleep(.5)
    print("\nSPINNING\n\n\n")
    time.sleep(.5)
    wallet = gamble(wallet)
    if start_response == "":
        while hasFunds(wallet):
            response = input("\n\nWant to spin again?\n\n")
            if response == "":
                print("\n\n\n\nSPINNING")
                time.sleep(.5)
                print("\nSPINNING")
                time.sleep(.5)
                print("\nSPINNING")
                time.sleep(.5)
                print("\nSPINNING")
                time.sleep(.5)
                print("\nSPINNING\n\n\n")
                time.sleep(.5)
                wallet = gamble(wallet)
            else:
                print("\n\n\n\naw, we really wanted to take the rest of your money.")
                break
        else:
            print("\n\n\nDang! You gambled all your money away.")
            time.sleep(2)
            print("\n\n\n...maybe you should go home and think about that.\n\n\n")
            time.sleep(2)


        

play(my_wallet)