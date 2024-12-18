print("welcom to the calculator of your classmate's score")
scorelist=input("enter the score of all student's score separeted by comma").split(',')
for n in range(0,len(scorelist)):
    scorelist[n]=int(scorelist[n])
total=0
for i in scorelist:
    if total < i:
        total=i
print(f'the heighest score is {total}')

