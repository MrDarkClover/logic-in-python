def sum(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s
res = sum(4)
print(res)

#time: o(n)
#space : o(1)