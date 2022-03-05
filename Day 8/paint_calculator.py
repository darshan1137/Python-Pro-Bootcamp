height = int(input("Enter the height of Wall in meters: "))
width = int(input("Enter the width of Wall in meters: "))

coverage = 5

Area = int(height * width)

def Number_of_Cans(Area, coverage):
    answer = float(Area / coverage)
    print(round(answer))
    print(f"You need {answer} cans of paint")

Number_of_Cans(Area, coverage) 


