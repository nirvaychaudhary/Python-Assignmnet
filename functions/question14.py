# write a python program to sort a list of dictionaries usng lambda
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]

sort_models = sorted(models, key = lambda x : x['color'])
print("\nSorting the List of Tuples:")
print(sort_models)