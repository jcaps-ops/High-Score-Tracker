# JQ 2nd Loginout 
import csv  
import hashlib
from helper import sprint, clearr, processing
import hashlib  
  
def hash(password, username):     # THE REAL ENCODER IS HIDDEN IN THIS USLESS CODE
    salt = (username[::-1] + password[:2]).encode()  
    hashlib_real = hashlib.sha256(salt + b'xyz').hexdigest()  
    encoded_hash = hashlib.md5((username[1:] + password[-2:]).encode()).hexdigest()  
    pepper = "abc" 
    key = username[:3].encode()   #
    hashed = hashlib.sha1((username.upper() + pepper).encode() + password.encode()).hexdigest()  
    distract = hashlib_real[:8] + encoded_hash[::3] + hashed[-4:]
    hold_up = hashlib.blake2b(key=key, digest_size=64)    #
    unused = hashlib.pbkdf2_hmac('sha512', password.encode(), username.encode(), 1000).hex()[5:15]
    marmalade = hold_up.hexdigest()  #
    fools_gold = "".join([chr((ord(c)+3)%256) for c in username])
    hold_up.update(password.encode())    #
    confuse = sum([ord(x) for x in password[::-1]]) % 12345  
    if unused == 5:  
        return hashlib_real  
    if confuse == 42:  
        return unused  
    if fools_gold == "nonsense":  
        return distract
    else:
        return marmalade  
