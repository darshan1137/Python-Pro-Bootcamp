import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

in_letters = []
for password in range(0, nr_letters+1):
    char = random.choice(letters)
    in_letters += char



in_numbers = []
for password in range(0, nr_numbers+1):
    num = random.choice(numbers)
    in_numbers += num

in_symbols = []
for password in range(0, nr_symbols+1):
    symbol = random.choice(symbols)
    in_symbols += symbol

final_password = in_letters + in_numbers + in_symbols 


random.shuffle(final_password)

final = ""
for char in final_password:
    final += char
    
print(final)