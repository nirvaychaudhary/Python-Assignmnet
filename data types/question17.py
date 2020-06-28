# write a python program to multiplies all the items in list. 
def multiply_func(lst):
    total = 1
    for i in lst:
        total = total * i
    return total
list1 = [1,2,3]     
print(multiply_func(list1))
