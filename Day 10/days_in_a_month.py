
def days_in_month(year, month):

    if int(year)%4 == 0 and month ==2:
        return 29

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    no_of_month = month -1
    return month_days[no_of_month]

year = int(input("Enter a year: "))
month = int(input("Enter the Month as a number: "))

days = days_in_month(year, month)

print(f"The Month has {days} days")
