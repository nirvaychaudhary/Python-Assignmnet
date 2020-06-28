# wtite a python function to insert a string in the middle of a string. 
# sample function and result:  
# insert_string_middle('[[]]<<>>', 'python')-> [[python]]
# insert_string_middle('{{}}', 'php')-> {{php}}

def insert_string_middle(tag, word):
    return tag[:2] + word + tag[2:]

print(insert_string_middle('[[]]', 'python'))
print(insert_string_middle('{{}}', 'php')) 