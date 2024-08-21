# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal),
# or scalene (no sides are equal). Use an if-else statement to classify the triangle.
# Logic building
# input=take input from user----- theree numbers ----int
# output= string
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if num2 == num1 == num3:
    print("All sides are equal so given triangle is equilateral")
elif num2 == num1 != num3:
    print("only two sides are equal so given triangle is isosceles")
elif num2 != num1 == num3:
    print("only two sides are equal so given triangle is isosceles")
elif num2 == num3 != num1:
    print("only two sides are equal so given triangle is isosceles")
else:
    print("No sides are equal so scalene")


