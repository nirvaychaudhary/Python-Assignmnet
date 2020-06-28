# write a python program to check whether all dictionaries
# in a list are empty or not.
# Sampe List: [{}, {}, {}]
# Return Value: True 
# Sampe List: [{1,2}, {}, {}]
# Return Value: False
  
empdict = [{}, {}, {}]
nonemp_dict = [{1,2}, {}, {}]
print(all(not value for value in empdict))
print(all(not value for value in nonemp_dict))

