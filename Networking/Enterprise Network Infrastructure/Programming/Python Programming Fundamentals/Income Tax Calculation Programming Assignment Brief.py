userAns="yes"
while (userAns.lower()== 'yes'):
    print ("Welcome to Commercia Tax System")
    Name=input("Add persons full name: ")
    Company=input("Add companies name: ")
    Income=float (input("Add your income: £"))
    if (Income <=20000):
            Tax=0
            Band= "Personal Allowance"
    elif (Income <=100000):
            Tax=(Income-20000)*0.2
            Band= "Basic Rate"
    else:
            Tax= (Income-100000)*0.45+16000 #16000=80000*0.2
            Band= "Additional Rate"
    print("Name of the company: ", Company)
    print("Name of the person: ", Name)
    print("The tax is: ", Tax)
    print("The tax band is: ", Band)
    print("The net pay is: ", Income-Tax)
    userAns=input("Input more? ")
print("Thank you for using Commercia Tax System. ")
