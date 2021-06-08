# Importing time module
from time import sleep
# Inputting the year
year_inputted = input("Enter the year which you want to check : ")
print("\n")
sleep(1)


def isLeapyear(year):
    year_list = list(year)
    if year_list[-1] == "0" and year_list[-2] == "0":
        if int(year) % 400 == 0:
            return True
        else:
            return False
    else:
        if int(year) % 4 == 0:
            return True
        else:
            return False


# The conditionals
output = isLeapyear(year_inputted)
if output:
    print("The given year is a leap year.")
else:
    print("The give year is not a leap year.")
