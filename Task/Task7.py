# Create a program that determines whether a given year is a leap year.
# hint A leap year is divisible by 4,
# but not by 100 unless it is also divisible by 400.

# Building logic
# Input---Take a input from user ----int
# Output--- string---either loop year or not
# Approach 1
# year = int(input("Enter the year"))
# if year % 4 == 0 and  year % 100 != 0  or year % 400 == 0 :
#      print(year," leap year")
# else:
#      print(year,"not a leap year")

#Approach 2
year = int(input("Enter the year"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a Leap year")
    else:
        print("leap year")
else:
    print("Not a leap year")


