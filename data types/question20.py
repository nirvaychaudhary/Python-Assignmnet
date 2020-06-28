# write a python program to count the number of string where the string length is
# 2 or more and the first and last character are same from a given list of strings.
# Sample List: ['abc', 'xyz', 'aba', '1221']
# expected result: 2

def count_string(word):
    count = 0
    for chars in word:
        if len(chars) > 1 and chars[:1] == chars[-1:]:
            count += 1
    return count
print(count_string(['abc', 'xyz', 'aba', '1221']))     
