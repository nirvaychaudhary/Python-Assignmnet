# write a python function that takes a list and returns a new unique elements of the first list
# Sample List: [1,2,3,3,3,3,4,5]
# Expected Result: [1,2,3,4,5]

def unique(elements):
    new_elements= []
    for i in elements:
        if i not in new_elements:
            new_elements.append(i)
    return new_elements
print(unique([1,2,3,3,3,3,4,5]))