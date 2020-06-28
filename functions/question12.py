# Write a python program to create a function that takes one argument and that 
# argument will be multiplied with an unkniwn given number. 

def mul_func(n):
    return lambda x: x * n
total = n=mul_func(2)
print("Double number of 15 = ", total(15))
total = n=mul_func(3)
print("Triple number of 15 = ", total(15))

