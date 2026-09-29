def arm(n):
    total=0
    digits = len(str(n))
    while n != 0:
        last = n % 10
        total+= last**digits 
        n //=10
    return total

n=9474
res= arm(n)
if res==n:
    print(f"{n} is armstrong")
else:
    print(f"{n} is not armstrong")

