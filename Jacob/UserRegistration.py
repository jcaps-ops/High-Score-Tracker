# JQ 2nd Loginout
import random as r  
import time as t  
import sys  
import csv  
import os
def clearr():  
    os.system('cls' if os.name == 'nt' else 'clear')  
def processing(text="Processing", duration=3, speed=0.5):
    end_time = t.time() + duration
    while t.time() < end_time:
        for dots in range(4):
            sys.stdout.write('\r' + text + '.' * dots + ' ' * (3 - dots))
            sys.stdout.flush() 
            t.sleep(speed)
    sys.stdout.write('\r' + ' ' * (len(text) + 3) + '\r')
    sys.stdout.flush()
    print(text)
def sprint(text, delay=0.025):  
    for char in text:  
        sys.stdout.write(char)  
        sys.stdout.flush()  
        t.sleep(delay)  
def pass_cheker():  
    special_characters = "!@#\$%^&*()_+-=[]{|;:,}.&lt;&gt;?)"  
    numbers = "1234567890"  
    while True:  
        password = input("\033[38;2;49;125;125mgood, now select your password\n").strip()  
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
            sprint("\033[38;2;255;1;1mPassword is not strong enough, WHat are you, a millenial?\n")  
            sprint("\033[38;2;255;1;1mMissing: " + ", ".join(errors) + "\n")  
        else:
            clearr()  
            sprint("\033[38;2;49;125;125mPassword is strong!\n")  
            return password  
def regis():  
    loop = True  
    while loop:  
        option = input("\033[38;2;49;125;125mWhat is your username? or type exit to exit\n").strip()  
        if option == "exit":
            clearr()  
            loop = False
            return 
              
        try:  
            with open("Jacob/pass_a_user.csv", mode="r+") as file:  
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
            try:  
                with open("Jacob/pass_a_user.csv", mode="a", newline='') as file:  
                    writer = csv.writer(file)  
                    writer.writerow([option, password])
                processing()
                clearr() 
                sprint("\033[38;2;49;125;125mUser added\n")  
             
            except:  
                sprint("\033[38;2;49;125;125mCould not write to file.")  
def login():  
    loop = True  
    while loop:  
        option = input("\033[38;2;0;125;1mWhat is your username? or type exit to exit\n").strip()  
        if option == "exit": 
            clearr() 
            loop = False  
            continue  
        try:  
            with open("Jacob/pass_a_user.csv", mode="r") as file:  
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
        print("\033[38;2;255;1;1mtry again")
        continue
