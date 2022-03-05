import random
from data import data 
from art import logo
from art import vs

print(logo)

no_of_attempts = 0
end = False


key_1 = int(random.randint(0, 49))



A = data[key_1]



while end == False:
    print(f"{A['name']} is a {A['description']} from {A['country']}")
    key_2 = int(random.randint(0,49))
    if key_1 == key_2:
        key_2 = int(random.randint(0,49))
    print(vs)
    B = data[key_2]
    print(f"{B['name']} is a {B['description']} from {B['country']}")


    condition = input("Type A or B whom you think has most followers: \n").upper()
    if A['follower_count'] > B['follower_count']:
        ans = 'A'
        print(f"\n{A['name']} is winner")
        if condition == ans:
            no_of_attempts += 1
            end = False
        else :
            print("Your Score is " + str(no_of_attempts))
            end = True
    else: 
        ans = 'B'
        print(f"\n{B['name']} is winner\n\n")
        if condition == ans:
            no_of_attempts += 1
            end = False
            A = data[key_2]
        else :
            print("\nYour Score is " + str(no_of_attempts))
            end = True

    
    




