print("welcome to calculator of GPA")
studentDictionary={
    "abel":69,
    "yohannes":95,
    "abbinet":89,
    "birhanu":79
}
for student in studentDictionary:
    if studentDictionary[student]>90:
        studentDictionary[student]="out-standing"
    elif studentDictionary[student]>80:
        studentDictionary[student]="excellent"
    elif studentDictionary[student]>70:
        studentDictionary[student]="above-expected"
    else:
        studentDictionary[student]="fail"
print(studentDictionary["abel"])

#nesting in dictionary
travelList=[
    {
        "country":"france",
        "cities":["marcey","parice","monaco"],
        "number":12
    },
    {
        "country":"ethiopia",
        'cities':["addis-ababa","debrezeyit","adama",],
        'number':20
    }
]
def addNewcountry(country,cities,number):
    newCountry={}
    newCountry["country"]=country
    newCountry["cities"]=cities
    newCountry["number"]=number
    travelList.append(newCountry)


addNewcountry("russia",["moscow","saint-petrsberg"],4)
print(travelList)