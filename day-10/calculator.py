oper=["+","-","*","/"]
finish=False
def calculator(number1,number2,operator):
    sum=0
    difference=0
    product=1
    qoutient=1
    if operator=='+':
        sum=number1+number2
        print(f"the sum of {number1} and {number2} is:{sum}")
    elif operator=='-':
        difference=number1-number2
        print(f"the difference of {number1} and {number2} is:{difference}")
    elif operator=='*':
        product=number1*number2
        print(f"the product of {number1} and {number2} is:{product}")
    elif operator=='/':
        qoutient=number1/number2
        return qoutient
while not finish:
    print("phytonist calculator")
    operand=int(input('enter the number'))
    for oper in oper:
        print(f"{oper}\n")
    operation=input("choose the operation")
    operand2=int(input('enter the number'))
    value=calculator(number1=operand,number2=operand2,operator=operation)
    print(value)