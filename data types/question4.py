''' Wite a python program to get a single string from the two given strings, seperated by space and swap the first two character of each string.
Sample String: 'abc', 'xyz'
Expected Result: 'xyc abz'
'''
def swap_func(a,b):
    swap_a = b[:2] + a[2:]
    swap_b = a[:2] + b[2:]
    return swap_a + " " + swap_b

print(swap_func('abc', 'xyz'))
