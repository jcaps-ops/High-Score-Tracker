import csv  
import hashlib
from helper import sprint, clearr, processing
import hashlib
from Jacob.hashable import hash
def login():  
    loop = True  
    while loop:  
        option = input("\033[38;2;0;125;1mWhat is your username? or type exit to exit\n").strip()  
        if option == "exit": 
            clearr() 
            loop = False  
            return 'exit'
        try:  
            with open("Documents/pass_a_user.csv", mode="r") as file:  
                reader = csv.reader(file, delimiter=',')                               
                users = {}                                      
                for line in reader:                             
                    users[line[0]] = line[1]                    
        except:                                                 
            sprint("\033[38;2;0;125;1mcant find csv\n")                              
            continue                                            
        if option in users: 
            processing()
            password = input("\033[38;2;0;125;1mEnter your password:\n").strip()
            if password == "exit" or password == "Exit":
                clearr()
                return password
            encripted_pass = hash(password, option)
            if encripted_pass == users[option]:  
                processing()
                clearr()
                sprint("\033[38;2;0;125;1mLogin successful!\n")
                return option 
            else: 
                clearr() 
                sprint("\033[38;2;255;1;1mIncorrect password, i thought you had an IQ higher than 85.\n")  
        else:  
            clearr()
            sprint("\033[38;2;255;1;1mYou Spell Like my grandma.\n")  