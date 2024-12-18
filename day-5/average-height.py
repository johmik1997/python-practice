print("welcom to the calculator of your classmate's height")
heightlist=input("enter the height of all student's height separeted by comma").split(',')
total=0
for height in heightlist:
    sum=int(height)
    total+=sum
average=total/len(heightlist)
print(f'the average height of your class student is {average}' )