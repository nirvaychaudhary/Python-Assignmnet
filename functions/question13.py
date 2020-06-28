# write a python program to sort a list of tuples using lambda
percentage = [('Tom', 55), ('jerry', 75), ('Bob', 65), ('Spike', 85)]
print("Original list of tuples:")
print(percentage)
percentage.sort(key = lambda x : x[1])
print("\nSorting the List of Tuples:")
print(percentage)
