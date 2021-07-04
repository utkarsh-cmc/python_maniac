from collections import Counter
a="aaabbbbbccccc"
my_counter=Counter(a)
print(my_counter)
print(my_counter.most_common(1)) #to acces the element print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))