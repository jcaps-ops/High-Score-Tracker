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
