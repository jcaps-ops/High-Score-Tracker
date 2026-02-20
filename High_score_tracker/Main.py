#This is the main file

from Jacob.UserRegistration import login, regis
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
