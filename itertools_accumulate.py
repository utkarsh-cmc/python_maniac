from itertools import accumulate
import operator #to do diff operation
a=[1,2,3,5,4]

acc=accumulate(a,func=operator.mul) #by default it counts the sum
print(list(acc))

acc=accumulate(a,func=max) #by default it counts the sum
print(list(acc))

