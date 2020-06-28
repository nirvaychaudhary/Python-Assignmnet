# Write a Python program to multiply all the items in a dictionary.
mydict = {'a': 1, 'b': 2, 'c': 3}
dict_values = mydict.values()
total = 1
for i in mydict:
    total = total * mydict[i]
print(total)