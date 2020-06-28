# write a python program to remove dublicate from a list
def remove(duplicate):
    new_list = []
    for num in duplicate:
        if num not in new_list:
            new_list.append(num)
    return new_list

print(remove([1,2,3,4,5,5,2,3,4])) 
