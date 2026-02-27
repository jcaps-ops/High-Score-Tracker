#This is the main file

from High_score_tracker.Jacob.logedin import login
from High_score_tracker.Jacob.regis import regis
from helper import sprint, clearr, processing
while True:
    ei = input("\033[38;2;0;125;1mlogin or register\n").strip().lower()
    if ei == "login":
        print(login()) 
    elif ei == "register": 
        print(regis())
    else:
        clearr()
        print("\033[38;2;255;1;1mtry again")
    
        continue
