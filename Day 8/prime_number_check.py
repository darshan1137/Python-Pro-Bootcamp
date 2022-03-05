""""
number = int(input("Enter the Number you want to check : "))

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It is a prime number")
    else:
        print("It is not a Prime Number")

prime_checker(number)"""

number = int(input("Enter the number you want to check : "))   
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
       if number % i ==0:
            is_prime = False

    if is_prime:
        print("it is a prime number ")
    else:
        print("it's not  a prime number ")

prime_checker(number)