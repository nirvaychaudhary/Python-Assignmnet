# write a python program to get the smallest number from list
num = int(input("Enter items: "))
mylist = []
for i in range(1, num+1):
    number = int(input("Enter Number: "))
    mylist.append(number)
    mylist.sort()
print("smallest number in list is: ", mylist[0]) 