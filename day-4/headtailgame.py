import random
chance=random.randint(0,1)
print("welcome to head and tail game")
userInput=input("enter the number either head or tail type: Head or Tail").lower()
if userInput=='head':
    if chance==1:
        print("computer draws Head")
        print("you won")
    else:
        print("you lose")

elif userInput=='tail':
    if chance==0:
        print("computer draws Head")
        print("you win")
        print("tail")
    else:
        print("you lose")
else:
    print("pls try again?")