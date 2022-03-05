year = input("Enter the Year: ")


check = int(year)%4

if check == 0:
    print(year + " is a Leap Year")
else:
    print(year + " is not a Leap Year")