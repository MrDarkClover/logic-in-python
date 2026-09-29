def sum(n):
    sq=0
    for i in range(1,n+1):
        sq+= i**2
    return sq
res=sum(2)
print(res)
#time : o(n)
#space : o(1)