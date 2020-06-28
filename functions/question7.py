# Write a python function that accepts a string and  calculate the number of
# uppercase letters and lowercase letters.
# Sample String: 'The quick Brow Fox'
# Expected Output: 
# No. Of uppercase Characters: 3
# No of Loewcase Characters: 12

def count_func(chars):
    char_dict = {"UPPERCASE": 0, "LOWERCASE": 0}

    for i in chars:
        if i.isupper():
            char_dict["UPPERCASE"] += 1
        elif i.islower():
            char_dict["LOWERCASE"] += 1
        else:
            pass

    print("original String: ", chars)
    print("No. of uppercase characters: ", char_dict["UPPERCASE"])
    print("No. of lowercase characters: ", char_dict["LOWERCASE"])
count_func('The quick Brow Fox')