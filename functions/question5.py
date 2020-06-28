# Write a python function to calculate the factorial of a number (a non-negative integer).
# the function that accepts the number as an argument.

n = int(input("Enter any num: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(n))