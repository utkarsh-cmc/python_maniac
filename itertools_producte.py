from itertools import product
a=[1,2]
b=[3,4]
prod=product(a,b)
print(list(prod))

'''
also we can do repeat parameter
'''
# a=[1,2]
# b=[3]
# prod=product(a,b,repeat=2)
# print(list(prod))