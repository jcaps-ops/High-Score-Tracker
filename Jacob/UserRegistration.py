# JQ 2nd Loginout
import random as r  
import time as t  
import sys  
import csv  
def processing(text="Processing", duration=3, speed=0.5):
    end_time = t.time() + duration
    while t.time() < end_time:
        for dots in range(4):
            # The carriage return '\r' moves the cursor to the start of the line
            # The 'end=""' prevents a new line from being printed
            sys.stdout.write('\r' + text + '.' * dots + ' ' * (3 - dots))
            sys.stdout.flush() # Forces the output to be written immediately
            t.sleep(speed)
    
    # Clear the final line and print a finish message
    sys.stdout.write('\r' + ' ' * (len(text) + 3) + '\r')
    sys.stdout.flush()
    print(text)
def sprint(text, delay=0.025):  
    for char in text:  
        sys.stdout.write(char)  
        sys.stdout.flush()  
        t.sleep(delay)  
def pass_cheker():
    password = input("what is your password \n").strip()  # ask for password and clean it  
    points = 0  # start points at zero  
  
    #length = len(password)  
    #list special_character  
    #list numbers  
    #characters is list(password)  
    #loop for letter in characters  
  
    special_characters = "!@#\$%^&*()_+-=[]{|;:,}.<>?)"  # all the weird symbols  
    numbers = "1234567890"  # just the digits for checking  
    # set up flags to see if each thing is found  
    has_num = False  # did we see a number yet  
    has_special = False  # did we see a special character yet  
    has_upper = False  # any uppercase found  
    has_lower = False  # any lowercase found  
  
    # go through each character in password  
    for char in password:  
        # if it's a number, remember that  
        if char in numbers:  
            has_num = True  
        # if it's a special, remember that  
        if char in special_characters:  
            has_special = True  
        # if uppercase, mark it  
        if char.isupper():  
            has_upper = True  
        # if lowercase, mark it  
        if char.islower():  
            has_lower = True  
  
    #if length >= 8 then points += 1  
    if len(password) >= 8:  # long enough  
        points += 1  
    #if has_num == True then points += 1  
    if has_num:  # saw a number  
        points += 1  
    #if has_special == True then points += 1  
    if has_special:  # saw a special char  
        points += 1  
    #if has_upper == True then points += 1  
    if has_upper:  # saw uppercase  
        points += 1  
    #if has_lower == True then points += 1  
    if has_lower:  # saw lowercase  
        points += 1  
  
    #Meeting the length requirement == True: +1 point  
    #Containing uppercase letters == True: +1 point  
    #Containing lowercase letters == True: +1 point  
    #Containing numbers == True: +1 point  
    #Containing special characters == True: +1 point  
    
    #if points == 1  
    if points == 1 or points == 2:  
        print("password is weak \n")  # say weak for 1 or 2  
        print(f"{points} point(s)")  
    #display password is medium  
    elif points == 3:  
        print("password is medium\n")  # 3 gets medium  
    #display password is good  
    elif points == 4:  
        print("password is good \n")  # 4 gets good  
    #display password is strong  
    elif points == 5:  
        print("password is strong \n")  # all 5, very strong  
    else:   
        print("please try again")  # no points, something went wrong  

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
            processing()
            password = input("\033[38;2;49;125;125mgood, now select your password\n")  
            try:  
                with open("Jacob/pass_a_user.csv", mode="a", newline='') as file:  
                    writer = csv.writer(file)  
                    writer.writerow([option, password])
                processing()  
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
            processing()
            password = input("\033[38;2;0;125;1mEnter your password:\n").strip()  
            if password == users[option]:  
                processing()
                sprint("\033[38;2;0;125;1mLogin successful!\n")
                return option 
            else:  
                sprint("\033[38;2;255;1;1mIncorrect password, i thought you had an IQ higher than 85.\n")  
        else:  
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
