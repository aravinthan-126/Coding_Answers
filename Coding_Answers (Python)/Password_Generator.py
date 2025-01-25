import random
a=int(input("Enter how many length of password did you want : "))
all="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-+=[]{};:<,>.?/|"
password="".join(random.sample(all,a))
print(password)