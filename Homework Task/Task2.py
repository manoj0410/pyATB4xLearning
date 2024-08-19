# Task 2
# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}
num1=int(input("Enter first number: \n"))
num2=int(input("Enter second number: \n"))

print(f"Maximum number is:{max(num1,num2)}")
print(f"Sum of Two number is: {num1+num2}")
print(f"Subtraction of two number is: {num1-num2}")
print(f"Multiplication of two number is: {num1*num2}")
print(f"Division of two number is: {num1/num2:.2f}")
print(f"Reminder of two number is: {num1%num2}")
print(f"Power of two number is: {num1**num2}")

