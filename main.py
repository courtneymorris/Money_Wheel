import random
import time
import sys
from termcolor import colored


def printRed(skk): print("\033[91m {}\033[00m" .format(skk))
def printGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def printYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def printLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def printPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def printCyan(skk): print("\033[96m {}\033[00m" .format(skk))


spin_cost = 5
winnings = 0
wheel = {
    0 : 20,
    1: 15,
    5 : 10,
    25 : 3,
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
        printYellow(f'\n\nCONGRATULATIONS!!!')
        time.sleep(.5)
        printPurple(f'\n\nYou\'ve WON ${winnings}! \n\nYou have ${wallet} left.')
    elif winnings > 0 and wallet < 5:
        printYellow(f'YAY!')
        printPurple(f'You won ${winnings}!\n\n')
        time.sleep(1)
        printPurple(". . .\n\n")
        time.sleep(1)
        printPurple(f'. . .but you only have ${wallet}, which isn\'t enough to play again.')
        time.sleep(1)
    elif winnings == 500:
        printGreen("JACKPOT!!!!!!!\n\n")
        time.sleep(.5)
        printYellow("You've won $500!!!!!")
    elif winnings == 0 and hasFunds(wallet):
        printRed(f'\n\nOOF, bad luck!')
        time.sleep(.5)
        printLightPurple(f'\nYou didn\'t win this time.')
        time.sleep(.5)
        printPurple(f'\nYou have ${wallet} left')
    
    return wallet



printYellow("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n WELCOME")
time.sleep(.5)
printGreen("         TO")
time.sleep(.5)
printPurple("             THE")
time.sleep(.5)

printCyan("                  C")
time.sleep(.25)
printLightPurple("                     A")
time.sleep(.25)
printGreen("                        S")
time.sleep(.25)
printRed("                           I")
time.sleep(.25)
printPurple("                              N")
time.sleep(.25)
printYellow("                                 O")
time.sleep(2)

my_wallet = int(input("\n\n\nHow much did you bring to gamble today?\n\n$"))
printLightPurple("\n\n\nWOW, big spender!")
time.sleep(.5)
printYellow("\nIt's just $5 to spin the wheel!")
time.sleep(1)
start_response = input("\n\nReady to spin?\n\n")


def play(wallet):
    printCyan("\n\n\n\nSPINNING")
    time.sleep(.25)
    printLightPurple("\nSPINNING")
    time.sleep(.25)
    printYellow("\nSPINNING")
    time.sleep(.25)
    printGreen("\nSPINNING")
    time.sleep(.25)
    printPurple("\nSPINNING")
    time.sleep(.25)
    printCyan("\nSPINNING")
    time.sleep(.25)
    printLightPurple("\nSPINNING")
    time.sleep(.25)
    printYellow("\nSPINNING")
    time.sleep(.25)
    printGreen("\nSPINNING")
    time.sleep(.25)
    printPurple("\nSPINNING\n\n\n")
    time.sleep(.25)

    wallet = gamble(wallet)

    if start_response == "":
        while hasFunds(wallet):
            response = input("\n\n\nWant to spin again?\n\n")
            if response == "":
                printCyan("\n\n\n\nSPINNING")
                time.sleep(.5)
                printLightPurple("\nSPINNING")
                time.sleep(.5)
                printYellow("\nSPINNING")
                time.sleep(.5)
                printGreen("\nSPINNING")
                time.sleep(.5)
                printPurple("\nSPINNING\n\n\n")
                time.sleep(.5)
                wallet = gamble(wallet)
            else:
                printYellow("\n\n\n\nAw man, we really wanted to take the rest of your money.\n\n\n")
                time.sleep(.5)
                printCyan("\n\n\n See you next time!\n\n\n\n\n\n\n")
                break
        else:
            printCyan("\n\n\nDang! I guess you gambled all your money away.")
            time.sleep(2)
            printPurple("\n\n\n...maybe you should go home and think about that.\n\n\n")
            time.sleep(2)



play(my_wallet)