# write a python program to create Fibonacci series upto n using lambda

from functools import reduce 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+ x[-2]], range(n-2), [0,1])
print("Fibnacci Series up to 5: ")
print(fib_series(5))
print("\n Fibonacci series up to 10: ")
print(fib_series(10))
