# The below program is computer vs singlr player Rock,Paper,scissor game(you can input the single player wish).
import random
a=["rock","paper","scissor"]
b=random.choice(a)
print("Choice your wish")
print("Enter the before number of your choice:")
print("0.rock,1.paper,2.scissor ")
c=a[int(input("your wish : "))]
print(c)
if(b==a[0] and c==a[2]) or (b==a[1] and c==a[0]) or (b==a[2] and c==a[1]):
    print("computer's wish : ",b)
    print("computer won")
elif(b==a[2] and c==a[0]) or (b==a[0] and c==a[1]) or (b==a[1] and c==a[2]):
    print("computer's wish : ",b)
    print('you won')
else:
    print("computer's wish : ",b)
    print("draw")

# The below program is 2 Players Rock,Paper,scissor game(we can input the two players wish).
a=["rock","paper","scissor"]
print("Player 1")
print("Choice your wish")
print("Enter the before number of your choice:")
print("0.rock,1.paper,2.scissor ")
b=a[int(input("your wish : "))]
print("Player 2")
print("Choice your wish")
print("Enter the before number of your choice:")
print("0.rock,1.paper,2.scissor ")
c=a[int(input("your wish : "))]
if(b==a[0] and c==a[2]) or (b==a[1] and c==a[0]) or (b==a[2] and c==a[1]):
    print("Player 1 won")
elif(b==a[2] and c==a[0]) or (b==a[0] and c==a[1]) or (b==a[1] and c==a[2]):
    print('Player 2 won')
else:
    print("draw")

# The below program is Player vs Computer Rock,Paper,scissor with Marks(you can input the player wish).
you=0
computer=0
def rockpaperscissor():
    global computer
    global you
    import random
    a=["rock","paper","scissor"]
    b=random.choice(a)
    print(b)
    print("Choice your wish")
    print("Enter the before number of your choice:")
    print("0.rock,1.paper,2.scissor ")
    c=a[int(input("your wish : "))]
    print(c)
    if(b==a[0] and c==a[2]) or (b==a[1] and c==a[0]) or (b==a[2] and c==a[1]):
        print("computer's wish : ",b)
        computer= computer+1
    elif(b==a[2] and c==a[0]) or (b==a[0] and c==a[1]) or (b==a[1] and c==a[2]):
        print("computer's wish : ",b)
        you=you+1
    else:
        print("Computer's Wish : ",b)
    print("\nDo you want play again..?")
    print("Then enter y for yes,n for no")
    d=input("Enter your choice : ")
    if d=='n':
        print("\nRESULT")
        print("computer=",computer)
        print("you=",you)
        if(computer>you):
            print("computer won")
        elif(computer<you):
            print("you won")
        else:
            print("Draw")
    else:
        rockpaperscissor()
rockpaperscissor()
