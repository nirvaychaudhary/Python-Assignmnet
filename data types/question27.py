# write a program to replace the last element in a list with another list.

# sample data = [1,3,4,7,9,10],[2,4,6,8]
# Expeted Output = [1,3,5,7,9,2,4,6,8]

list1 = [1,3,4,7,9,10]
list2 = [2,4,6,8]
list1[-1:] = list2
print(list1) 