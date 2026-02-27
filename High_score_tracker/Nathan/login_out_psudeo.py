#NH 2nd login logout psuedocode

#def login function
#   Make an infinite loop
#       Ask for their username
#       Check if they wanted to leave by typing exit (So it's compatible with Jacob's exit strat)
#           Cut off the function from it's loop
#       make a try and accept to read the file
#       try
#           With open(Relative path of the file reading mode) all as file
#           Do the same stuff from the notes all the way down
#       If the option they gave is in users    
#           Ask for password
#           if password in passwords
#               display the login as successful
#           Optionally break here if user wants to stop after a successful login by using the same exit strat
#       otherwise if user gives invalid password:
#           display username as invalid
# JQ 2nd Loginout 
import csv  
import hashlib as h
from helper import sprint, clearr, processing
# functions used everywhere^^^^^

def regis():
    def pass_cheker():  
        special_characters = "!@#\$%^&*()_+-=[]{|;:,}.><?)"  
        numbers = "1234567890"  
        while True:  
            password = input("\033[38;2;49;125;125mgood, now select your password, or type exit to exit\n").strip()
            if password == "exit" or password == "Exit":
                return password
            errors = []  
            if len(password) < 8:  
                errors.append("at least 8 characters")  
            if not any(char in numbers for char in password):  
                errors.append("a number")  
            if not any(char in special_characters for char in password):  
                errors.append("a special character")  
            if not any(char.isupper() for char in password):  
                errors.append("an uppercase letter")  
            if not any(char.islower() for char in password):  
                errors.append("a lowercase letter")  
            
            if errors:
                clearr()  
                sprint("\033[38;2;255;1;1mPassword is not strong enough, What are you, a millenial?🤣\n")  
                sprint("\033[38;2;255;1;1mMissing: " + ", ".join(errors) + "\n")  
            else:
                clearr()  
                sprint("\033[38;2;49;125;125mPassword is strong!\n")  
                return password   
    loop = True  
    while loop:  
        option = input("\033[38;2;49;125;125mWhat is your username? or type exit to exit\n").strip()  
        if option == "exit":
            clearr()  
            loop = False
            return 
              
        try:  
            with open("Documents/pass_a_user.csv", mode="r+") as file:  
                reader = csv.reader(file, delimiter=',')   
                users = []  
                for line in reader:  
                    users.append({line[0]: line[1]})  
        except:  
            sprint("\033[38;2;49;125;125mcant find csv")  
            continue  
        found = False  
        for user in users:  
            if option in user:
                clearr()
                sprint("\033[38;2;255;1;1malready in data base\n")  
                found = True  
                break  
        if not found:  
            processing()
            password = pass_cheker()
            ''
            ''
            ''
            if password == "exit" or password == "Exit":
                clearr()  
                loop = False
                return 
            try:  
                with open("Documents/pass_a_user.csv", mode="a", newline='') as file:  
                    writer = csv.writer(file)  
                    writer.writerow([option, password])
                processing()
                clearr() 
                sprint("\033[38;2;49;125;125mUser added\n")
                
             
            except:  
                sprint("\033[38;2;49;125;125mCould not write to file.")  
            return option  
def login():  
    loop = True  
    while loop:  
        option = input("\033[38;2;0;125;1mWhat is your username? or type exit to exit\n").strip()  
        if option == "exit": 
            clearr() 
            loop = False  
            continue  
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
            if password == users[option]:  
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
while True:
    ei = input("\033[38;2;0;125;1mlogin or register\n").strip().lower()
    if ei == "login":
        print(login()) 
    elif ei == "register":
        
        regis()
    else:
        clearr()
        print("\033[38;2;255;1;1mtry again")
    
        continue
