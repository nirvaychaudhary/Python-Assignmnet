# write a python function that takes number as a parameter and check the number is prime or not.
# Note: A prime number (or a prime) is a natiral number greater than 1 and that has no positive divisors other than 1 and itself.

number = int(input("ENter any number: "))
def primenumber(num):
    if(num == 1):
        return False

    elif(num == 2):
        return True

    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

print(primenumber(number))