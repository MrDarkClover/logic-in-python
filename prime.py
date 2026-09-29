import math as m
def prime(n):
    if n < 2:
        is_prime= False
    # else:
    #     is_prime = True

    #     for i in range(2,n):
    #         if n % i == 0:
    #             is_prime=False
    #             break
    # return is_prime    

    for i in range(2, m.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
res=prime(55)
if res == True:
    print("it is prime")
else:
    print("not a prime")


#time : O(n)
#space : O(1)