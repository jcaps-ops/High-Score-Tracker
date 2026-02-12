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

  
import csv  

def regis():  
    loop = True  
    while loop:  
        option = input("What is your username?\n").strip()  
        if option == "exit":  
            loop = False  
              
        try:  
            with open("Jacob/pass_a_user.csv", mode="r+") as file:  
                reader = csv.reader(file, delimiter=',')   
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
                with open("Jacob/pass_a_user.csv", mode="a", newline='') as file:  
                    writer = csv.writer(file)  
                    writer.writerow([option, password])  
                print("User added")  
             
            except:  
                print("Could not write to file.")  

regis()

  
