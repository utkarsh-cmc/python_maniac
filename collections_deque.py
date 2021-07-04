from collections import deque
d=deque()

d.append(1)
d.append(2)
d.appendleft(3) 
print(d)
d.extend([4,5,6])
print(d)
d.pop()
print(d)
d.rotate(2) #can give -ve to rotate left
print(d)