#In the below code is used to check if the given number is perfect number or not.
#Perfect Number : Sum of the perfectly divident of the given number is equal to the given number.
#For example-(If given number is 6,the perfectly divident are (1,2,3) and their sum is 6 which is equal to given number).
a=int(input("Enter a number to check it is perfect number or not : "))
count=0
for i in range(1,a):
    if(a%i==0):
        count=count+i
if(count==a):
    print("The given number",a,"is a perfect number")
else:
    print("The given number",a,"is a not perfect number")