# write a python script to add a key to a dictionary. 
# Sample Dictionary: {0:10, 1:20}
# Expected Result: {0:10, 1:20, 2:30} 

mydict = {0:10, 1:20}
mydict.update({2:30})
print(mydict)
  