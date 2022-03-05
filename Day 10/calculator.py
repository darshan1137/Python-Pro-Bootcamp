def add(no1, no2):
    return no1 + no2

def sub(no1, no2):
    return no1 - no2

def divide(no1, no2):
    return no1 / no2

def multiply(no1, no2):
    return no1 * no2

operations  = {
"+" : add,
"-" : sub,
"*" : multiply,
"/" : divide

}

end_of_game = False

logo = '''
 _____         _               _         _               
/  __ \       | |             | |       | |              
| /  \/  __ _ | |  ___  _   _ | |  __ _ | |_  ___   _ __ 
| |     / _` || | / __|| | | || | / _` || __|/ _ \ | '__|
| \__/\| (_| || || (__ | |_| || || (_| || |_| (_) || |   
 \____/ \__,_||_| \___| \__,_||_| \__,_| \__|\___/ |_|   
                                                         
                                                         
'''
print(logo)
for i in operations:
    print(i)

main = int(input("Enter the Start Number: "))
while end_of_game == False:

    start = input("Enter the Operation: ")
    next = int(input("Enter the Next Number: "))

    if start == "+":
        answer = add(main, next)
    elif start == "-":
        answer = sub(main, next)
    elif start == "/":
        answer = divide(main, next)
    elif start == "*":
        answer = multiply(main, next)
    else:
        print("Invalid")

    print(f"{main} {start} {next} = {answer}")
    condition = input("Enter 'Y' to continue and 'N' To Quit: \n")
    if condition == "Y":
        main = answer
        end_of_game = False

    else:
        end_of_game = True