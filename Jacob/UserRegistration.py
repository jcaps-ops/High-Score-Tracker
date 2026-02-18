# JQ 2nd Loginout
#import csv  
#  
#define regis() as a function:  
#    loop is equal to True  
#    while loop is true:  
#        option is equal to display "What is your username? 
#        if option is equal to exit:  
#            loop is equal to False  
#            return  
#        try:  
#            open pass_a_user.csv mode r as file  
#                reader is equal to csv.reader(file, delimiter=',')   
#                users is a list  
#                for line in reader:  
#                    append line[0]: line[1] to users
#        except:  
#           display cant find csv  
#           continue  
#        found is equlat to False  
#        for user in users:  
#            if option is in user:  
#                display already in data base  
#                found is equal to True  
#                break  
#        if found is false:  
#            password is equal to display  good, now select your password  
#            try:  
#                 open pass_a_user.csv mode="a newline is space, as file:  
#                    writer is equal to csv.writer(file)  
#                    writer.writerow([option, password])  
#                display User added  
#             
#            except:  
#                display Could not write to file  
#
#run function regis()
import random as r  
import time as t  
import sys  
  
def sprint(text, delay=0.025):  
    for char in text:  
        sys.stdout.write(char)  
        sys.stdout.flush()  
        t.sleep(delay)  
import csv  

def regis():  
    loop = True  
    while loop:  
        option = input("\033[38;2;49;125;125mWhat is your username? or type exit to exit\n").strip()  
        if option == "exit":  
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
                sprint("\033[38;2;255;1;1malready in data base\n")  
                found = True  
                break  
        if not found:  
            password = input("\033[38;2;49;125;125mgood, now select your password\n")  
            try:  
                with open("Jacob/pass_a_user.csv", mode="a", newline='') as file:  
                    writer = csv.writer(file)  
                    writer.writerow([option, password])  
                sprint("\033[38;2;49;125;125mUser added\n")  
             
            except:  
                sprint("\033[38;2;49;125;125mCould not write to file.")  



def login():  
    loop = True  
    while loop:  
        option = input("\033[38;2;0;125;1mWhat is your username? or type exit to exit\n").strip()  
        if option == "exit":  
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
            password = input("\033[38;2;0;125;1mEnter your password:\n").strip()  
            if password == users[option]:  
                sprint("\033[38;2;0;125;1mLogin successful!\n")
                username = option
                return username  
            else:  
                sprint("\033[38;2;255;1;1mIncorrect password, i thought you had an IQ higher than 85.\n")  
        else:  
            sprint("\033[38;2;255;1;1mYou Spell Like my grandma.\n")  
while True:
    ei = input("\033[38;2;0;125;1mlogin or register\n").strip().lower()
    if ei == "login":
        login() 
    elif ei == "register":
        username = regis()
    else:
        print("\033[38;2;255;1;1mtry again")
        continue

# mol,man