#This is the main file for high score tracker. AS NH JQ JC 2nd
#Import everything
from Jacob.logedin import login
from Jacob.regis import regis
from helper import sprint, clearr, processing
from Aiden.Tracker import score_tracking, highscores
from Jaxon.CasinoRoyale import game

#While loop
while True:
    #Main menu
    ei = input("\033[38;2;0;125;1m1: login\n2: register\n3: play (this will not save your score, for you did not log in)\n4: view leaderboard\n5: leave\n").strip().lower()

    #login
    if ei == "1":
        username = login()
        if username == 'exit' or username == 'Exit':
            continue
        else:
            pass
        score_tracking(username, game())

    #registration
    elif ei == "2": 
        username = regis()
        if username == 'exit' or username == 'Exit':
            continue
        else:
            pass
        score_tracking(username, game())
    
    #play game
    elif ei == "3": 
        game()
    
    #View leaderboard
    elif ei == "4": 
        clearr()
        highscores()
        print('\n\n')
        continue

    #leave
    elif ei == "5": 
        break

    #if invalid
    else:
        clearr()
        print("\033[38;2;255;1;1mtry again")
    #Make sure user knows to have big terminal
        continue
    print("Please use full screen")
    
    #Display the high scores
    highscores()

    #While loop
    while True:
        #Ask them what they want for after the game
        uinput = input("Would you like to 1: Play Again, or 2: Leave?\n").strip()
        #If they wanna play again
        if uinput == '1':
            try:
                #Display the score
                score_tracking(username, game())
                highscores()
            #Start the game
            except:
                game()
                highscores()
        #leave the game
        elif uinput == '2':
            break
        else:
            print("Invalid input.")
            continue