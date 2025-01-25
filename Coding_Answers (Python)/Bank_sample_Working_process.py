account_number=None
amount=0
def registration():
    global account_number,amount
    name=input("Enter your Name : ")
    account_number=input("Enter your Account NUmber : ")
    phone_number=input("Enter your phone number : ")
    amount=int(input("Enter a basic amount which is greater than rs.500 : "))
    while amount < 500 :
        print("The amount must be greater than Rs.500")
        amount=int(input("Enter a valid amount : "))
    print("\n Registration Successfully! Welcome",name)
def check_balance():
    global amount
    print("\n Your Current balance : ",amount)
def deposit():
    global amount
    deposit=int(input("Enter the amount to deposit : "))
    amount=amount+deposit
    print("\n Deposited Amount : ",deposit,"\n Deposited Successfully..!")
def withdraw():
    global amount
    withdraw=int(input("Enter the amount to withdraw : "))
    while amount < withdraw :
        print("Insufficient Amount")
        withdraw=int(input("Enter the valid amount to withdraw : "))
    amount=amount-withdraw
    print("\n Withdraw Amount : ",withdraw,"\n Withdraw Successfully..!")
def exit_program():
    print("\n Thank for visiting Bank.")
    exit()
while True:
    print("\n1.Restration. \n2.check Balance. \n3.Deposit. \n4.Withdraw. \n5.Exit.")
    a=int(input("Enter your choice in the prefix number : "))
    if a==1:
        registration()
    elif a==2:
        check_balance()
    elif a==3:
        deposit()
    elif a==4:
        withdraw()
    elif a==5:
        exit_program()
    else:
        print("Invalid Choice,Please try again")