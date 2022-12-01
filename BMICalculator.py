height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI=round((weight/(height**2)))
if BMI<18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI>=18.5 and BMI<25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI>=25 and BMI<30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI>=30 and BMI<35:
    print(f"Your BMI is {BMI}, you are obese.")
elif BMI>=35:
    print(f"Your BMI is {BMI}, you are clinically obese.")
