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
def login():
    loop = True
    while loop == True:
        option = input("What is your username?\n").strip()
        if option == "exit":
            loop = False
        try:
            with open("pass_a_user.csv",mode = "r") as file:
                reader = csv.reader(file,delimiter=',')
                header = next(reader)
                users = []
                for line in reader:
                    users.append(
                        {
                            line[0]:line[1],
                            
                        }
                    )
        except:
            print("cant find csp")
        else:
            for user in users:
                if option in user:
                    print("already in data base")
                    break
                
                password = input("good, now select your password")
        try:
            with open("pass_a_user.csv",mode = "r") as file:
                reader = csv.reader(file,delimiter=',')
        except:
            print("something went wrong")

login()