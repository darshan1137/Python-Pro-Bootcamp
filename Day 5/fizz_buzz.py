
for i in range (1, 101):
    if i%3 == 0 and i%5 == 0:
        i = "FizzBUzz"
    elif i%3 ==0:
        i = "Fizz"
    elif i%5 == 0:
        i = "Buzz"
    print(i)