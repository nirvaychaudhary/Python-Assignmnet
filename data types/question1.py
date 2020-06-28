''' write a python program to count the number of characters (character frequency) in a string
    Sample string : google.com'
    Expected Result : {'0' : 3, 'g' : 2 ,'.' : 1, 'l':1, 'm':1, 'c':1}
'''
# Solution

def character_frequency(str):
    dict = {}
    for num in str:
        keys = dict.keys()
        if num in keys:
            dict[num] += 1
        else:
            dict[num] = 1
    return dict
print(character_frequency('google.com'))

