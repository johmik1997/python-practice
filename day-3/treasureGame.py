print("welcome to treasure island\n your tresure is to find treasure")
direction=input(" you are at crros road ,where do want to go left or right")
dirr=direction.lower()
if dirr=='left':
    print("game over")
elif dirr=='right':
    ch2=input("do you want to swim or wait type 'swim' or 'wait' ").lower()
    if ch2=='swim':
        print("br hungry corocodile ,you are attack game over")
    elif ch2=='wait':
        ch3=input("you arrive at island . there is ahouse with 3 doors. one red one yellow and one blue what color do you choose?").lower()
        if ch3=='red':
            print('this room is full of fire ,game over')
        elif ch3=='blue':
            print('you found the treasure. you win')
        else:
            print("you are in correct pls try again later")
    else:
        print("you are in correct pls try again later")    
else:
    print("you are in correct pls try again later")    