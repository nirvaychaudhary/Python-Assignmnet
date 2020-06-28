# write a python program to check whether a given string is number or not using lambda

num = lambda n:n.replace('.', '', 1).isdigit()
print(num('125678'))
print(num('3.141414'))
print(num('-45789'))
print(num('00'))
print(num('abcd1234'))
print('\n print checking numbers: ')

num1 = lambda r: num(r[1:]) if r[0] == '-' else num(r)
print(num1('-45'))
print(num1('-12.5'))
