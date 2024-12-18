import random
print("welcome to the rock-paper-scissor game")
computerMove=''
randomValue=random.randint(1,9)
print(computerMove)
if randomValue >=1 and randomValue<=3:
    computerMove='rock'
elif randomValue>3 and randomValue<=6:
    computerMove='paper'
else:
    computerMove='scissor'
userMove=input('enter your move type either ROCK,PAPER OR SCISSOR :').lower()
print('computer moves '+computerMove)
if userMove=='rock':
    if computerMove=='paper':
        print('you lose')
    elif computerMove=='paper':
        print('you win')
    else:
        print('draw')
elif userMove=='paper':
    if computerMove=='rock':
        print('you win')
    elif computerMove=='paper':
        print('draw')
    else:  
        print('you lose')
elif userMove=='scissor':
   
    if computerMove=='rock':
        print('you lose')
    elif computerMove=='paper':
        print('you win')
    else:  
        print('draw')   
print('thanks for your visting my site')
