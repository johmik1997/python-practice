print("welcome to my co") #this
height =int(input("enter your height?"))
bill=0
if height>120:
    print("yo are greater than 120cm")
    age =int(input("enter your age?"))
    if age<12:
        print("you have to paid $5 ticket")
        bill=5
    elif age<=  18:
        print("you should pay $7 ticket")
        bill=7
    elif age<22:
        print("you should pay $10 ticket")
        bill=10
    else: 
        print("you have to paid  $12   ticket")  
        bill=12 
    want_photo=input("do you want a photo? y or n . ")
    if want_photo=='y':
        bill+=3
        print(f"{bill} is your bill")
    else:
        print("your bill is the same because of you don't want a photo")
else:
    print("you have not growth enough")    