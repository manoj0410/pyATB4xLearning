# FizzBuzz Test:
# Write a program that prints numbers from 1 to 100. # Loop
# For However, for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz."
# For numbers that are multiples of both 3 and 5, print "FizzBuzz."

# logic building
# input --- int---print number from 1 to 100
# output--- string---if multiple of 3--Fizz, Multiple of 5--Buzz and
# if multiple of 3 and 5 then FizzBuzz else number
import math
Fizz_count=0
Buzz_count=0
FizzBuzz_count=0
number_count=0
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print(num,"FizzBuzz")
        FizzBuzz_count += 1 #Increment counter when FizzBuzz is printed
    elif num % 5 == 0:
        print(num,"Buzz")
        Buzz_count += 1
    elif num % 3 == 0:
        print(num,"Fizz")
        Fizz_count += 1
    else:
        print(num,"Number")
        number_count += 1

print("Total FizzBuzz occurrences",FizzBuzz_count)
print("Total Fizz occurrences",Fizz_count)
print("Total Buzz occurrences",Buzz_count)
print("Total Number occurrences",number_count)