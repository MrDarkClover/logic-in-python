import random as rd
def dice(n):
    # if(n == 6):
    #     return 1
    # elif(n == 5):
    #     return 2
    # if(n == 4):
    #     return 3
    # elif(n == 3):
    #     return 4 
    # if(n == 2):
    #     return 5
    # elif(n == 1):
    #     return 6

    return 7 - n
n=rd.randint(1,6)
res=dice(n)
print(f"{n}'s opposite :{res}")
#time: o(6) / o(1)
#space : o(1)