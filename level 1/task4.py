#user input of numbers in operation
n1=int(input("enter the first number: "))
n2=int(input("enter the first number: "))

#user input of operator in operation
op=input("enetr the operator(+,-,*,/,%): ")


#conditional satements to compare operators
if(op=="+"):

    #storing value of operation in result variable
    result=n1+n2

    #printing the operation
    print(n1,"+",n2,"=",result)

elif(op=="-"):
    result=n1-n2
    print(n1,"-",n2,"=",result)

elif(op=="*"):
    result=n1*n2
    print(n1,"*",n2,"=",result)

elif(op=="/"):
    result=n1/n2
    print(n1,"/",n2,"=",result) 

elif(op=="%"):
    result=n1%n2
    print(n1,"%",n2,"=",result)    

else:

    #prints following messeage if any invalid operator
    print("invalid operator") 
