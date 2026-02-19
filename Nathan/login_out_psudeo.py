#NH 2nd login logout psuedocode

#def login function
#   Make an infinite loop
#       Ask for their username
#       Check if they wanted to leave by typing exit (So it's compatible with Jacob's exit strat)
#           Cut off the function from it's loop
#       make a try and accept to read the file
#       try
#           With open(Relative path of the file reading mode) all as file
#           Do the same stuff from the notes all the way down
#       If the option they gave is in users    
#           Ask for password
#           if password in passwords
#               display the login as successful
#           Optionally break here if user wants to stop after a successful login by using the same exit strat
#       otherwise if user gives invalid password:
#           display username as invalid
