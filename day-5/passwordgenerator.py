import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
character=['!','@','#','$','%','^','&','*','(',')']
number=['1','2','3','4','5','6','7','8','9','0']
num_letter=int(input('enter the number of letter on your password'))
num_character=int(input('enter the number of character on your password'))
num=int(input('enter the number of numbers on your password'))
password=[]
order=[2,1,5,3,6,4]
final=''
for pas in range(1,num_letter+1):
    password.append(random.choice(letter))
for pas in range(1,num_character+1):
    password.append(random.choice(character))
for pas in range(1,num):
    password.append(random.choice(number))
# print(password)
# count = len(password)
# for char in order:
#     final+=password[char]
# print(final)
random.shuffle(password)
for char in password:
    final+=char
print(final)