import re 

#function to validate email
def validtest(string):

    #creating a regular expression as email format
    e_format=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    #comparing user email with the format
    if(re.match(e_format,string)):
        print("valid email")
    else:
        print("invalid email")  


#user email input
string=input("enter a email: ")

#calling validate function
validtest(string)