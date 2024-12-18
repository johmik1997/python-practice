import random
print("welcome back")
name=input("enter everybody's name separated by comma :")
namelist=name.split(',')
chance=random.randint(0,len(namelist)-1)
print(namelist[chance] + " is going pay bill today")