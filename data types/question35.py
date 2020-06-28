# Write a Python program to iterate over dictionaries using for loops.
d = {'math': 80, 'science': 75, 'english': 90, 'Nepali': 85}
for sub_key, value in d.items():
    print(sub_key, 'corresponds to', d[sub_key])