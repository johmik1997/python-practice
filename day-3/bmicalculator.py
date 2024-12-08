print("welcom to my BMI calculator")

weight=float(input("enter your weight in kg:"))
height=float(input("enter your height"))
BMI=round(weight/(height**2))
if BMI<18.5:
    print(f"your BMI IS {BMI} you are underweight")
elif BMI<25:
    print(f"your BMI IS {BMI} you have a normal weight")
elif BMI<30:
    print(f"your BMI IS {BMI} you are overweight")
elif BMI<35:
    print(f"your BMI IS {BMI} you are obese")
else:
    print(f"your BMI IS {BMI} you are clinically obese")
