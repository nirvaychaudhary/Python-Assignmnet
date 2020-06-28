# write a python function to check whether a number is in a given range.
user= int(input("Eter any number to check it is in a range or not: "))
def num_range(nums):
    if nums in range(1,5):
        return "%s is in range" %str(nums)
    else:
        return "%s is out of range" %str(nums)
print(num_range(user))  
