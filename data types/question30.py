# write a python script to check whether a given key already exists in a dictionary.

mydict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def findkey_func(x):
    if x in mydict:
        print('Key is present in this dictionary')
    else:
        print('Key is no present in this dictionary')

findkey_func(3)
findkey_func(7)