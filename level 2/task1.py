import random

#generates random number and assigns to r_num
r_num=random.randint(1,100)

#user guesssing of random number
user_num=int(input("enter the guessed number: "))


#while loop  run infinite time until break statement is encountered
while(1):

    #comparing user input and generated number
    if(r_num==user_num):
        print("Nice! your guess is right")
        print("number is",r_num)
        break

    elif(user_num<r_num):
        print("Hint: too low, try again!")
        user_num=int(input("enter the guessed number: "))
        continue
    
    elif(user_num>r_num):
        print("Hint: too high, try again!")
        user_num=int(input("enter the guessed number: "))
        continue