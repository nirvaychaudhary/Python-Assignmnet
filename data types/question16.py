# write a python program to sum all the utems in a list

num = int(input("Enter items: "))
total = []
for i in range(num):
    numbers = int(input('Enter numbers to sum: '))
    total.append(numbers)
print("sum of given items is: ", sum(total))