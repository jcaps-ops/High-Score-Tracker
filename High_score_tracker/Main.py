#This is the main file

from Jacob.logedin import login
from Jacob.regis import regis
from helper import sprint, clearr, processing
from Aiden.Tracker import score_tracking, highscores
from Jaxon.CasinoRoyale import game

while True:

    ei = input("\033[38;2;0;125;1mlogin or register\n").strip().lower()
    if ei == "login":
        username = login()
        print(username) 
    elif ei == "register": 
        username = regis()
        if username == 'exit' or username == 'Exit':
            continue
        else:
            pass
    else:
        clearr()
        print("\033[38;2;255;1;1mtry again")
    
        continue
    print("Please use full screen")
    score_tracking(game(), username)

    highscores()

    while True:
        uinput = input("Would you like to 1: Play Again, or 2: Leave?\n").strip()
        if uinput == '1':
            score_tracking(game(), username)
            highscores()
        elif uinput == '2':
            break
        else:
            print("Invalid input.")
            continue