# write a python program to insert a given string at the begining of all items in list. 
# Sample List: [1,2,3,4], string: emp
# Expected Output: ['emp1', 'emp2', 'emp3', 'emp4']

def preinsert(list, str):
    str += '{0}'
    list = [str.format(i) for i in list]
    return (list)

list = [1,2,3,4]
str = 'emp'
print(preinsert(list,str))
