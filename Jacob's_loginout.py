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
    try:
        with open("Main.py","r+", newline ='') as test:
            reader = csv.reader(test,delimiter=',')
            header = next(reader)
            users = []
            for line in reader:
                users.append(
                    {
                       header[0]: line[0],
                       header[1]: line[1],
                       header[2]: line[2],
                  }
             )
    except:
        print("failed to open")
    else:
       try:
            temp_user = input("ask user what their username is\n").strip().lower()
            pass_location = users.find(temp_user)
       except:
             print("try again")
             return username
login()