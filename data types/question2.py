''' Write a python program to get a string made of the first 2 nad last 2 chars from a given a string. if the string length is less than 2, return instead of the empty string. 
Sample String: 'python'
Expected Result: 'pyon'
Sample String: 'py'
Expected Result: 'pypy'
Sample String: 'w'  
Expected Result: Empty String
'''
user = input("Enter the word: ")
def str_function(str):
    if len(str) >= 2:
        return str[0:2] + str[-2:]
    else:
        return ''
print(str_function(user))
print(str_function('py'))
print(str_function('w'))
    


