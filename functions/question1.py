# write a python function to find max of three numbers. 

def max_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
print(max_num(4,2,-5))
