temp=0
def game(a):
    global temp
    c=str(a)
    for i in range(0,len(str(a))+1):
        b=c[i]
        print(b)
        temp+=(int(b))
        if temp==1:
            print("Magical number")
        elif temp==0 or a>1 and a<=9:
            print("Not Magical number")
        else:
            game(temp)
b=int(input("Enter a number to check if it is Magical number or nor : "))
game(b)