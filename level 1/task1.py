#function which returns reversed string
def rev(string):
        string_rev=string[::-1]
        return string_rev

#string input from the user
string= input("enter a string: ")

#calling string revrse function and assigning value to String2
string2=rev(string)

#printing reversed string
print("reverse of string:",string2)


