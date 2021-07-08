def sumofN(n):
    if n<=1:
        return 1
    else:
        return n + sumofN(n-1)

num=5
print(str(sumofN(num)))        
