def rev(n):
    r=0
    while n != 0:
        last = n % 10
        r=r *10 +last
        n //= 10
    return r
res=rev(54321)
print(res)