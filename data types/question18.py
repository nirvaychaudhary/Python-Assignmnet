# write a python program to find the largest number in list

num = int(input("Enter items: "))
mylist = []
for i in range(1, num+1):
    list1 = int(input("Enter the items: "))
    mylist.append(list1)
print("Largest num in list is: ", max(mylist))
