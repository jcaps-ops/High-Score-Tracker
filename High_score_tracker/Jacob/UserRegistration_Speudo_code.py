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
