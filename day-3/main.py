print("welcome to my co") #this
height =int(input("enter your height?"))

if height>120:

    print("yo are greater than 120cm")
    age =int(input("enter your age?"))
    if age<12:
        print("you have to paid $5 ticket")
    elif age<=  18:
        print("you should pay $7 ticket")
    elif age<22:
        print("you should pay $10 ticket")
    elif age>45 & age<60:
        print("everyting is free")
    else: 
        print("you have to paid  $12   ticket")    
else:
    print("you have not growth enough")     