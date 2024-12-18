print("welcome to the love calculator")
name1=input("what is your name? ") 
name2=input("what is your darling's name? ")
sum1=0
sum=0
fullname=name1+name2
sum+=fullname.lower().count('t')
sum+=fullname.lower().count('r')
sum+=fullname.lower().count('u')
sum+=fullname.lower().count('e')
sum1+=fullname.lower().count('l')
sum1+=fullname.lower().count('o')
sum1+=fullname.lower().count('v')
sum1+=fullname.lower().count('e')
love_score=str(sum)+str(sum1)
print(love_score)
score= int(love_score)
if score <10 or score>90:
    print(f"your score is {score} , you together like coke and mentos")
elif score >=40 and score <=65:
    print(f"your score is:{score}, you are alright together")
else:
    print(f"your score is{score}")

