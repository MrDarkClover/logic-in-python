def palin(n):
    rev= 0

    while n != 0:
        last = n % 10
        rev = rev * 10 + last
        n //=10
    print(rev)
    return rev
n=1214
res= palin(n)
if n == res:
    print(f"{n} is a palindrome. ")
else:
    print(f"{n} is a not palindrome. ")