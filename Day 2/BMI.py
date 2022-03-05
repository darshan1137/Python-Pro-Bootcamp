height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

kg = int(weight)
m = float(height)

BMI = int(kg/(m**2))

print(BMI)