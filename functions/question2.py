# Write a python function to sum all numbers in a list. 
# Sample List: (8,2,3,0,7)
# Expected Output: 20

def sum_func(mysum):
    totalsum = 0
    for i in mysum:
        totalsum += i
    return totalsum
print(sum_func([8,2,3,0,7]))
