def digit_root(n):
    total=0

    while n != 0:
        last = n % 10
        total += last
        n //= 10
 
    return total

res = digit_root(99999)
t=0
while res != 0:
    last = res % 10
    t += last
    res //= 10
print(t)