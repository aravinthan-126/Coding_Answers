computer=0
you=0
def game():
    global computer
    global you
    import random
    a1=["pyton","sql","ruby","go","swift","kotlin","perl","rust","grails","lua","matlab","dart","erlang","clojure","julia","basic","html","css","react","django","flask","vue","blazor","gatsby","symfony","phalcon","bash","pyramid","julia",'ada']
    a2=["cut","copy","paste","alt","ctrl","tab","shift","undo","redo","save","saveas","open","find","bold","color","paint","close","print","find","edit","sort","view","share","backup","run","compile","align","sync","shutdown","export"]  
    a3=["computer","mouse","cloud","algorithm","compile","debug","encryption","decryption","network","data","hyperlink","storage","proxy","terminal","schema","bit","byte","bug","boot","binary","font","file","code","editor","widget","drive","host","input","desktop","domain"] 
    a4=['cpu', 'gui', 'ram', 'rom', 'ssd', 'hdd', 'http', 'bios', 'ip', 'dns', 'ftp', 'tcp', 'udp', 'os', 'gui', 'cli', 'api', 'ide', 'sdk', 'i/o', 'ai', 'ml', 'json', 'xml', 'sql', 'dns', 'usb', 'pdf', 'url', 'ssh']
    choice1=["a1","a2","a3","a4"]
    choice2=random.choice(choice1)
    if choice2=='a1':
        intro()
        print("The word is from programming language")
        a=list(random.choice(a1))
    elif choice2=='a2':
        intro()
        print("The word is from application and computer operations")
        a=list(random.choice(a2)) 
    elif choice2=='a3':
            intro()
            print("The word is from computer components and the computer general words")
            a=list(random.choice(a3))
    else:
        intro()
        print("The word is from computer abbrivation words")
        a=list(random.choice(a4))
    print("you have",len(a)-1,"chances")
    b=random.choice(a)
    c=(a.index(b))
    d=list(len(a)*"-")
    d[c]=b
    print(" ".join(d))
    attempt=0
    if(attempt<=len(a)-1):
        for i in range(len(a)-1):
            e=list(input("enter a char :"))
            for j in range(len(a)):
                if(a[j]==e[0]):
                    f=a.index(a[j])
                    g= " ".join( e ) 
                    d[f]=g
                    print(" ".join(d))
            attempt=attempt+1
    h=0
    for k in range(len(d)):
        if(d[k]=='-'):
            h=h+1
    if(h>0):
        print("The correct answer is"," ".join( a ))
        computer=computer+1
    else:
        print("The answer is correct")
        you=you+1
    print("you want to play or not.If yes then enter y.If No then enter n")
    i=input("Enter your choice : ")
    if i=='y':
        game()
    else:
        exit
def intro():
    print("welcome to computer relavent word find game.")
    print("The character in the word cannot be repeated.")
game()
print("\n")
print("RESULT")
print("computer = ",computer)
print("you = ",you)
if computer==you:
    print("Draw")
elif computer > you:
    print("Computer Wins")
else:
    print("You win")