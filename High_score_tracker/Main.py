#This is the main file

from Jacob.logedin import login
from Jacob.regis import regis
from helper import sprint, clearr, processing
from Aiden.Tracker import score_tracking, highscores
from Jaxon.CasinoRoyale import game

while True:
    ei = input("\033[38;2;0;125;1m1: login\n2: register\n3: play (this will not save your score, for you did not log in)\n4: view leaderboard\n5: leave\n").strip().lower()
    if ei == "1":
        username = login()
        if username == 'exit' or username == 'Exit':
            continue
        else:
            pass
        score_tracking(username, game())

    elif ei == "2": 
        username = regis()
        if username == 'exit' or username == 'Exit':
            continue
        else:
            pass
        score_tracking(username, game())
    
    elif ei == "3": 
        game()
    
    elif ei == "4": 
        clearr()
        highscores()
        print('\n\n')
        continue

    elif ei == "5": 
        break

    else:
        clearr()
        print("\033[38;2;255;1;1mtry again")
    
        continue
    print("Please use full screen")
    

    highscores()

    while True:
        uinput = input("Would you like to 1: Play Again, or 2: Leave?\n").strip()
        if uinput == '1':
            try:
                score_tracking(username, game())
                highscores()
            except:
                game()
                highscores
        elif uinput == '2':
            break
        else:
            print("Invalid input.")
            continue