#function which produces fibonacci sequence...0,1,(0+1)....((n-1)+(n-2))
def fibo(n):
    n1=0
    n2=1
    for i in range(0,n):
        if(i==0):
            print("0",end=" ")
        elif(i==1):
            print("1",end=" ")
        elif(i>1):
            next_num=n1+n2
            print(next_num,end=" ")
            n1=n2
            n2=next_num


#user input 
n=int(input("enter the of number terms in fibonacci series: "))

#function call
fibo(n) 