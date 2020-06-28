'''Write a python program to get a string from a given string where all occurances of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''
user = input("Enter word: ")
def replace_fun(str):
    char = str[0]
    str  = str.replace(char, '$') #replace char
    str = char + str[1:]
    return str

print(replace_fun(user)) 