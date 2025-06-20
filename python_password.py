##special password


import re

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%*!])\S{8,}$"


password1 = input('enter your password. must be at least 8 characters long, must have one special character (@#$%*!), must have letters and numbers, and must have at least one upper case and one lower case letter: ')
    
if re.match(pattern, password1):
    print('strong password')
    
else:
    print('this is invalid')
    

