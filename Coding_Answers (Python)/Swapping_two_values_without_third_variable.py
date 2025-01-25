#In the below code explains swapping of values from a variable without using the third variable
a=int(input("Enter the first number : "))
b=int(input("enter the second number : "))
print("Before swapping : ","a =",a,"b =",b)
a=a+b
b=a-b
a=a-b
print("After swapping : ","a =",a,"b =",b)