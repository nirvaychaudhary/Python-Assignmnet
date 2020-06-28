# write a python program to remove the nth index character from nonempty string.
def remove_index(str1, n):
    first = str1[:n]
    last = str1[n+1:]
    return first + last

print(remove_index('apple', 2))