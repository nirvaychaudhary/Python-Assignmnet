# write a python script to generate and print dictionary that contains a number (between 1 and n) in the form(x, x*x). 
# Sample Dictionary (n=5)
# Expected Output : {1: 2, 2: 4, 3: 9, 4: 16, 5:25}   
n = int(input("ENter any number: "))
d = dict()
for x in range(1,n+1):
    d[x] = x * x
print(d)
