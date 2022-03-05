import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

x = len(names)

number = random.randint(0, x-1)

bill_name = names[number]

print(bill_name + " will pay the bill")