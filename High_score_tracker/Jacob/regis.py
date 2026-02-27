# JQ 2nd Loginout 
import csv  
import hashlib
from helper import sprint, clearr, processing
import hashlib  
from hash import hash
from High_score_tracker.Jacob.logedin import login
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
            encripted_pass = hash(password,option)
            if password == "exit" or password == "Exit":
                clearr()  
                loop = False
                return 
            try:  
                with open("Documents/pass_a_user.csv", mode="a", newline='') as file:  
                    writer = csv.writer(file)  
                    writer.writerow([option, encripted_pass])
                processing()
                clearr() 
                sprint("\033[38;2;49;125;125mUser added\n")
                
             
            except:  
                sprint("\033[38;2;49;125;125mCould not write to file.")  
            return option  