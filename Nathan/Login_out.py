#NH 2nd Login Logout pseudocode
#import csv
import csv
#def the login function
def login():  
    #Make an infinite loop
    loop = True  
    while loop:  
        #Ask for their username
        option = input("What is your username?\n").strip()  
        #Check if they wanted to leave
        if option == "exit":  
            #Cut off the function from it's loop
            loop = False  
            #continue
            continue  
        #make a try and accept to read the file
        #try
        try:  
            #With open(Relative path of the file) reading mode all as file
            with open("pass_a_user.csv", mode="r") as file:  
                #Do the same stuff from the notes all the way down
                reader = csv.reader(file, delimiter=',')        #
                header = next(reader)                           #
                users = {}                                      #
                for line in reader:                             #
                    users[line[0]] = line[1]                    #
        except:                                                 #
            print("cant find csv")                              #
            continue                                            #
        #If the option they gave is in users
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
