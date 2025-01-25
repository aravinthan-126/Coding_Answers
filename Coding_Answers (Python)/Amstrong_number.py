#The below program is to find the given number is amstrong number or not.
#amstrong number is the sum of the power of the digits in the actual number(153)
a=int(input("Enter a number to check if it is amstrong number or not : "))
sum=0
temp=a
while temp>0 :
    digit=temp%10
    sum+=digit**3
    temp//=10
if a==sum:
    print("Given number is a amstrong number")
else:
    print("Given number is not an amstrong number")
