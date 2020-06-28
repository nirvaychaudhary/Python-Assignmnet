# write a python function to create HTML string with tags around the words(s).
# Sample Function and result:
# add_tags("i", 'python')-> '<i>Python</i>'
# add_tags("b", 'python tutorial')-> '<b> Python Tutorial </b>'

def add_tag(tag, word):
    return "<%s> %s </%s>" %(tag, word, tag)

print(add_tag("i", "python"))
print(add_tag("b", "Python Tutorial"))