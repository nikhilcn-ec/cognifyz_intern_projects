import random

print("\t\t\t\t\tWelcome to Number Guessing Game")

#taking lower and upper bound of the range
lb=int(input("enter lowerbound of range: "))
ub=int(input("enter upperbound of range: "))

#generate random number in sepcified range
ran_num=random.randint(lb,ub)

#user guessing of random number
guess=int(input("enter the guessed number: "))


#while loop run infinite time until break statement is encountered
while(1):

    #comparing user input and generated number
    if(guess==ran_num):
        print("Congratulations! your guess is right")
        break

    elif(guess<ran_num):
        print("too low, try again!")
        guess=int(input("enter the guessed number: "))
        continue
    
    elif(guess>ran_num):
        print("too high,try agaIn!")
        guess=int(input("enter the guessed number: "))
        continue