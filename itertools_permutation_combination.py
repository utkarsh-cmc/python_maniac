from itertools import combinations_with_replacement, permutations,combinations
a=[1,2,3,4]
p=permutations(a) #can give arg to permutations(a,2)
# print(list(p))

c= combinations(a,2)
print(list(c))

#to get combination with same element we can use ->

cwr=combinations_with_replacement(a,2)
print(list(cwr))