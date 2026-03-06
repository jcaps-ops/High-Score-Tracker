# JQ 2nd Loginout 
import csv  
import hashlib
from helper import sprint, clearr, processing
import hashlib  
  
def hash(password, username):     # THE REAL ENCODER IS HIDDEN IN THIS USLESS CODE
    key = username[:3].encode()   #
    hold_up = hashlib.blake2b(key=key, digest_size=64)    #
    marmalade = hold_up.hexdigest()  #
    hold_up.update(password.encode())    #
    return marmalade  
