print("welcome to an identifying a leap year")
continued=False
def identifyLeapyr(yearnumber):
    if year % 4 ==0:
        if year %100 ==0:
            if year % 400 ==0: 
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def daysInmonth(year,month):
    month_in_day=[31,28,31,30,31,31,30,30,31,30,31]
    if identifyLeapyr and month==2:
        return 29
    return month_in_day[month-1]
while not continued:
    print("leap year, that identify wether the year is leap or not")
    year=int(input("enter the year"))
    month=int(input("enter the month"))
    output=daysInmonth(year,month)
    print(output)
    tocontinue=input("do you want to continue type 'yes' or 'no' ")
    if tocontinue=='no':
        continued=True
    else:
        continued=False
