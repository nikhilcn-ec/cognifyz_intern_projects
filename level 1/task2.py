#temperature value input from user
tempvalue=int(input("enter the value of temperature: "))

#unit value input from user
unit=input("enter the unit of temperature(C/F): ")


#comparing unit values 
if(unit.lower()=="c"):

    #converting clesius to fahrenheit
    v1=(tempvalue*9/5)+32
    print(f'{tempvalue}{chr(176)}{unit} is converted to {round(v1,2)}{chr(176)}F')


elif(unit.lower()=="f"):

    #converting fhrenheit to celsius
    v1=(tempvalue-32)*5/9
    print(f'{tempvalue}{chr(176)}{unit} is converted to {round(v1,2)}{chr(176)}C')


else:

    #prints this messeage if unit is other than celsius or fahrenheit
    print("invalid unit")