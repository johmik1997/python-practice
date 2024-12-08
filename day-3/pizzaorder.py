print("welcom to python pizza delivery")
size=input("what size piza do yuo want? S,M,or L  ")
addsieson=input("do want any pepperioni? Y or N ")
add_cheese=input("do you want any extra chhese? Y or N ")
bill=0
if size=='S':
    bill+=15
elif size=='M':
    bill+=20
else:
    bill+=25
if addsieson=='Y':
    if size=='S':
        bill +=2
    else:
        bill+=3
       
if add_cheese=='Y':
    bill+=1
print(f"your final biil is {bill}")
