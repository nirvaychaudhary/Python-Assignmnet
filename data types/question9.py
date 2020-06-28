# write a python program to change a given string to a new string 
# where the first and last chars have been exchanged.

def exchange(str1):
    swap = str1[-1:] + str1[1:-1] + str1[:1]
    return swap

print(exchange("Hello"))