# write a python function to multiplty all number in a list.
# sample list: (8,2,3,-1,-7)
# Expected Output: -336
#

def multi_func(number):
    total = 1
    for i in number:
        total = total * i
    return total
print(multi_func([8,2,3,1,-7]))