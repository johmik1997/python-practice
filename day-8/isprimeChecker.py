number=int(input('enter the number to check if it\'s prime or not: '))
def primeChecker(number):
    isprime=True
    for i in range(2,number-1):
        if number%i==0:
            isprime=False
    if isprime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
primeChecker(number)