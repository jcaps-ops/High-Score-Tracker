#This is the main file

from Jacob.logedin import login
from Jacob.regis import regis
from helper import sprint, clearr, processing
from Aiden.Tracker import score_tracking, highscores
from Jaxon.CasinoRoyale import 

while True:
    ei = input("\033[38;2;0;125;1mlogin or register\n").strip().lower()
    if ei == "login":
        username = login()
        print(username) 
    elif ei == "register": 
        username = regis()
        print(username) 
    else:
        clearr()
        print("\033[38;2;255;1;1mtry again")
    
        continue
    
    score_tracking()