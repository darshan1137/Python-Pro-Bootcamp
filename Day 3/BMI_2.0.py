height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

kg = int(weight)
m = float(height)

BMI = int(kg/(m**2))

print(BMI)

if BMI>35:
    print("You are Clinically Obese")
elif BMI> 30:
    print("You are Obese")
elif BMI > 25:
    print("You are Overweight")
elif BMI >18.5:
    print("You have a normal Weight")
elif BMI < 18.5:
    print("You are Underweight")