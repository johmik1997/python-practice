continued=False
def identifyLeapyr(yearnumber):
    if year % 4 ==0:
        if year %100 ==0:
            if year % 400 ==0: 
                return f"{year} this is a leap year"
            else:
                return f"{year} is not leap" 
        else:
            return f"{year} is  leap year"
    else:
        return f"{year} is not leap year"
    

while not continued:
    print("leap year, that identify wether the year is leap or not")
    year=int(input("enter the year"))
    output=identifyLeapyr(yearnumber=year)
    print(output)
    tocontinue=input("do you want to continue type 'yes' or 'no' ")
    if tocontinue=='no':
        continued=True
    else:
        continued=False



   
       
          
        
    