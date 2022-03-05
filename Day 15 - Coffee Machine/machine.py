MENU = {
    "espresso": {        
        "water": 50,
        "coffee": 18,
        "cost": 1.5,
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5,
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,   
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

quit_machine = False
money = 0

while not quit_machine:
    print("Welcome to Coffe Machine")
    coffee = input("What would you like (espresso, latte, cappuccino): ").lower()

    if coffee == "quit":
        print("Thankyou! Visit Again")
        quit_machine = True

    elif coffee == "report":
        print(f"Water: {resources['water']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Milk: {resources['milk']}")
        print(f"Money: {money}")
        quit_machine = False

    no_of_quaters = int(input("Enter number of quaters you want to insert: "))
    no_of_dimes = int(input("Enter number ofdimes you want to insert: "))
    no_of_nickles = int(input("Enter number of nickles you want to insert: "))
    no_of_pennies = int(input("Enter number of pennies you want to insert: "))

    total_amount = (no_of_quaters * 0.25) + (no_of_dimes * 0.10) + (no_of_pennies * 0.01) + (no_of_nickles * 0.05)

    if coffee == 'espresso':
        soln = MENU["espresso"]
        if soln['cost'] < total_amount :
            change = round(total_amount - soln['cost'], 2)
            print(f"Here is your Change: ${change} ")
            print(f"Enjoy your {coffee}")

        elif soln['cost'] > total_amount:
            print("Insufficient Money")
            print(f"Here is your Refund: ${total_amount} ")            
            quit_machine = False

        money += soln['cost']
        resources["water"] -= soln['water']
        resources["coffee"] -= soln['coffee']

    elif coffee == "latte":
        soln = MENU["latte"]
        if soln['cost'] < total_amount :
            change = round(total_amount - soln['cost'], 2)
            print(f"Here is your Change: ${change} ")
            print(f"Enjoy your {coffee}")

        elif soln['cost'] > total_amount:
            print("Insufficient Money")
            print(f"Here is your Refund: ${total_amount} ")            
            quit_machine = False

        money += soln['cost']
        resources["water"] -= soln['water']
        resources["coffee"] -= soln['coffee']
        resources["milk"] -= soln['milk']

    elif coffee == "capppuccino":
        soln = MENU["cappuccino"]
        if soln['cost'] < total_amount :
            change = round(total_amount - soln['cost'], 2)
            print(f"Here is your Change: ${change} ")
            print(f"Enjoy your {coffee}")

        elif soln['cost'] > total_amount:
            print("Insufficient Money")
            print(f"Here is your Refund: ${total_amount} ")
            quit_machine = False

        money += soln['cost']
        resources["water"] -= soln['water']
        resources["coffee"] -= soln['coffee']
        resources["milk"] -= soln['milk']

    

    
    
        

