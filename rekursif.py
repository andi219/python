def pangkat(x,n):
    if n ==1:
        return x
    else:
        return x * pangkat(x, n-1)
    
x = int(input())
n = int(input())
print(pangkat(x,n))