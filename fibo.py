n=int(input("Enter the number: "))
a=0
b=1
if n >= 1:
    print(a)

if n >= 2:
    print(b)
c=0
for i in range(2, n):
    c = a + b
    print(c)
    a = b
    b = c