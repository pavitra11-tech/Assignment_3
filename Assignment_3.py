# Task:1 calculating the factorial of a number

def factorial(number):
    if number==1:
        return 1

    else:
        result = number*factorial(number-1)
        return result

number = float(input("Enter the number: "))

factorial = number*factorial(number-1)
print(f"Factorial of {number} is {factorial}")


# Task:2 Using the Math Module for Calculations

import math

def square_root(number):
    return math.sqrt(number)

def logarithm(number):
    return math.log(number)

def sine(number):
    return math.sin(number)

number = float(input("Enter the number: "))

print(f"Square root: {square_root(number)}")
print(f"Logarithm: {math.log(number)}")
print(f"Sine: {math.sin(number)}")
