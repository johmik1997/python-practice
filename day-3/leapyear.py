print("leap year, that identify wether the year is leap or not")
year=int(input("enter the year"))
if year % 4 ==0:
    if year %100 ==0:
        if year % 400 ==0: 
            print(f"{year} this is a leap year")
        else:
            print(f"{year} is not leap") 
    else:
        print(f"{year} is  leap year") 
else:
    print(f"{year} is not leap year")



   
       
          
        
    