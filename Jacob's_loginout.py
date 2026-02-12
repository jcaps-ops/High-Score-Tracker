# JQ 2nd Loginout
#define login function
#   try to open csv file
#        reader = csv.reader(sample,delimiter=',')
#        header = next(reader)
#        users = []
#        for line in reader:
#            users.append(
#                {
#                    header[0]: line[0],
#                    header[1]: line[1],
#                    header[2]: line[2],
#                }
#            )
#   except display "failed to open"
#   else:
#       try:
#           tem_user is ask user what their username is 
#           pass_location  is user.find(temp_user)
#       except:
#             display try again
#               return username is 0

import csv  
  
def regis():  
    loop = True  
    while loop:  
        option = input("What is your username?\n").strip()  
        if option == "exit":  
            loop = False  
            continue  
        try:  
            with open("pass_a_user.csv", mode="r") as file:  
                reader = csv.reader(file, delimiter=',')  
                header = next(reader)  
                users = []  
                for line in reader:  
                    users.append({line[0]: line[1]})  
        except:  
            print("cant find csv")  
            continue  
        found = False  
        for user in users:  
            if option in user:  
                print("already in data base")  
                found = True  
                break  
        if not found:  
            password = input("good, now select your password\n")  
            try:  
                with open("pass_a_user.csv", mode="a", newline='') as file:  
                    writer = csv.writer(file)  
                    writer.writerow([option, password])  
                print("User added")  
             
            except:  
                print("Could not write to file.")  

regis()

  
def login():  
    loop = True  
    while loop:  
        option = input("What is your username?\n").strip()  
        if option == "exit":  
            loop = False  
            continue  
        try:  
            with open("pass_a_user.csv", mode="r") as file:  
                reader = csv.reader(file, delimiter=',')  
                header = next(reader)  
                users = {}  
                for line in reader:  
                    users[line[0]] = line[1]  
        except:  
            print("cant find csv")  
            continue  
  
        if option in users:  
            password = input("Enter your password:\n").strip()  
            if password == users[option]:  
                print("Login successful!")  
                # Optionally break here if you want to stop after a successful login  
            else:  
                print("Incorrect password.")  
        else:  
            print("Username not found.")  
  
login()  
