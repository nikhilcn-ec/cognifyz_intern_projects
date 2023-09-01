
#functions checks if the given string is planidrome
def ispalindrome(s):

    #compares string and its reversed srting
    if(s==s[::-1]):
        print(s,"is a palindrome")
    else:
        print(s,"is not a plaindrome")

#user input of string
string=input("enter a word: ")

#calling the ispalindrome function
ispalindrome(string)