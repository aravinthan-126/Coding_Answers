# The below program is to find the given input as palindrome(121=121,mom=mom (actual value == reversed value))
# The below progam taken as integer input as string and gives the correct answer.
a=input("enter a value for che is it palindrome : ")
b=a[::-1]
if(a==b):
    print("it is palindrome")
else:
    print("it is not palindrome")
#Another version for palindrome
a=input("enter a value for che is it palindrome : ")
b=a[::-1]
c="it is palindrome" if a==b else "it is not palindrome"
print(c)