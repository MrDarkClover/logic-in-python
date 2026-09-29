def evenodd(num):
    for i in num:
        if i % 2 != 0:
            return False
    return True

num = [2, 4, 6, 8, 10, 12]

res = evenodd(num)

if res:
    print("all are even")
else:
    print("odd present in array")
#time: o(n)
#space: o(1)