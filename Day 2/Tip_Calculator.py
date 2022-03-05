print("Welcome to the Tip Calculator")
Total_amount = input("Please Enter the Total Bill Amount\n₹ ")
Tip_percentage = input("What percentage tip would you like to give?\n")
No_of_people = input("How many number of people to split the Bill\n")

Net_amount = int(Total_amount) + (float(Tip_percentage)/100*float(Total_amount))

per_person = int(Net_amount)/int(No_of_people)

print(f"Each person should pay: ₹ {per_person}")