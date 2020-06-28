# Write a python program to print even numbers from a given list. 
# Sample list : [1,2,3,4,5,6,7,8,9]
# Expected Result: [2,4,6,8]

mylist = [1,2,3,4,5,6,7,8,9]

even_list = list(filter(lambda x: (x%2 == 0), mylist))
print("Even list: ", even_list)