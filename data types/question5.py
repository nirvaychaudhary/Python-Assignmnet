'''Write a python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given striing already ends with 'ing' then add 'ly' instead. if the string length of the given string is less than 3,
leave it unchanged. 
Sample String: 'abc'
Expected Result: 'abcing'

Sample String: 'string'
Expected Result: 'stringly'
'''
def adding(str1):
    if len(str1) > 2:
        if str1[-3:] == 'ing':
            return str1 + "ly"
        return str1 +"ing"

    else:
        return str1 
print(adding("abc"))
print(adding('string'))
print(adding("hi"))
