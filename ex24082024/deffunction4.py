# Lambda Expression : a lambad is an autonoums function that retuns some form of data
import math


def Give_me_power(num):
    return math.pow(num,2)
power_num= Give_me_power(10)
print(power_num)

o=lambda num: math.pow(10,2)
print(o(10))

o=lambda : math.pow(int(input("Enter a number\n")),2)
print(o())