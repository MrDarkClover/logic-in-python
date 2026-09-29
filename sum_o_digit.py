def digit(n):
        sum=0
        while n != 0:
                last = n % 10 
                sum += last 
                n //= 10
        return sum
res= digit(43215)
print(res)

#time : o(log n)
#space : o(1)