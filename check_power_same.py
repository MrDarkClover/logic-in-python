def check_power(x,y):

    x**=2

    if x == y:
        return True

    return False

x=2
y=4
res=check_power(x,y)
if res==True:
    print(f"{x} is a square of {y}")
else:
    print(f"{x} is a not square of {y}")

#time: O(n)
#space: O(1)