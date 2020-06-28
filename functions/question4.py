# write a python program to reverse a string
def reverse_str(str1):
    new_str = ''
    index = len(str1)
    while index > 0:
        new_str = new_str + str1[index -1]
        index = index - 1
    return new_str
print(reverse_str(['1234abcd']))