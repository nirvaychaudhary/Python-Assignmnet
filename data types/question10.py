# write a python program to remove the characters which have odd index value in given string

def odd_index(str1):
    new_str = " "
    for i in range (len(str1)):
       if i % 2 == 0:
            new_str = new_str + str1[i]
    return new_str

print(odd_index("Hello"))