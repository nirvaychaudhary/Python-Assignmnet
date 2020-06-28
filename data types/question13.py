# write a python program that accepts a comma separated sequence of words 
# as input and prints the unique words in sorted from (alphanumerically).
# Sample Words: red, white, black, red, green, black
# Expected Result: black, green, red, white, red    

user = input("Input comma seperated sequence of words: ")
words = [word for word in user.split(",")]
print(",".join(reversed(list(words))))