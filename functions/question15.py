# write a python program to filter a list of integer using lambda

numbers = [1,2,3,4,5,6,7,8,9,10]
print("Original list is: ")
print(numbers)

even_nums = list(filter(lambda x : x%2 == 0, numbers))
print("\n Even number of list is: ")
print(even_nums)

odd_nums = list(filter(lambda x : x%2 != 0, numbers))
print("\n Odd number of list is: ")
print(odd_nums)
