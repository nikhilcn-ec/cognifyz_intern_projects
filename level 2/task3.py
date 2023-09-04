import re
 

#function to evaluate password
def evaluate(p):

    #checks for length
    if(len(p)<8):
        return -1
    
    #checks for uppercase letters
    elif not re.search(r'[A-Z]',p):
        return -1
    
    #checks for lowercase letters
    elif not re.search(r'[a-z]',p):
        return -1
    
    #checks for digits
    elif not re.search(r'[0-9]',p):
        return -1
    
    #checks for special characters
    elif not re.search(r'[!@#$%^&*()-+]',p):
        return -1

    
 #user input
password=input("enter the password: ")

#calling evaluate functions
value=evaluate(password)

#checking if password is valid or not
if(value==-1):
    print("invalid password")
else:
    print("valid password")
