#Fibonacci series in for loop (In the series print the number of times given in the input number.)
# (For example the input number is 10,it prints the first 10 number in the series)
c=int(input("Enter how many numbers in the fibonacci serie : "))
a,b=0,1
for i in range(c):
    print(a)
    a,b=b,a+b
#Fibonacci series in while loop (In the series print upto given input number.)
# (For example the input number is 10,it prints series upto 10)
c=int(input("Enter a number for printing upto the fibonacci series : "))
a,b=0,1
while a<c :
    print(a)
    a,b=b,a+b
    