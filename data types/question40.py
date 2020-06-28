# write a python program to add an item in a tuple
tuple1 = (1,2,3,4,5,6)
print(tuple)

tuple1 = tuple1 + (7,)
print(tuple1)

# adding items in specific index
tuple1 = tuple1[:3] + (0, 8, 9) + tuple1[:5]
print(tuple1)

# by converting tuple in list
list1 = list(tuple1)
list1.append(-5)
tuple1 = tuple(list1)
print(tuple1)
