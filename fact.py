def fact(n):
    for i in range(1,n):
        n *= i
    return n
n=int(input("Enter the number: "))
res= fact(n)
print(res)

#time: O(n)
#space: O(1)