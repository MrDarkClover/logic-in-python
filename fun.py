# def hello():
#     print("yo")

# hello()

# def addi(x,y):
#     print(x+y)

# addi(2,3)

# def palin(n):
#     rev=0
#     while n != 0:
#         lst= n % 10
#         rev = rev * 10 + lst
#         n//=10

#     return rev

# x=12321
# res = palin(x)
# if x == res:
#     print("palindrome")


# def mul(a,b):
#     print(a*b)

# mul(9,0)

# def mul(a=2,b=3):
#     print(a*b)

# mul()

# def mul(a,b):
#     print(a*b)

# mul(b=9,a=9)


# ------------------------------------Data Structure ----------------------------------------------------------------------------------
# a=[12,232,43,245,532,445]
# print(type(a))

# a[1]=22
# a.append(55)
# a.insert(1,22)
# # a.remove(22)
# lst=a.pop(0)
# print(lst)
# print(a)

# pos=[]
# neg=[]
# def arr(a):

#     for i in a:
#         if i < 0:
#             neg.append(i)
#         else :
#             pos.append(i)
#     return pos,neg

# res= arr([3,-1,4,-5,9])
# print(pos,neg)

# mean= 0
# def avg(n):
#     sum=0
#     size=len(n)
#     for i in n:
#         sum+=i
#     mean = (sum//size)
#     return mean

# print(avg([10,20,30,40]))


# def great(n):
#     large=n[0]
#     idx=0
#     for i in range(len(n)):
#         if n[i] > large :
#             large= n[i]
#             idx=i
#     return large,idx
# print(great([4,8,2,9,1]))

# def great(n):
#     large=n[0]
#     sec=n[0]
#     for i in range(len(n)):
#         if n[i] > large :
#             sec = large
#             large= n[i]
#     return sec
# print(great([4,8,2,9,1]))

# ----------------------tuple-----------------------

# a=(1,2,3,'o','p')
# print(a)
# l=list(a)
# print(l)

# print(a.index(3))
# print(a.count(3))



#----------------------set-------------------------------
# s={}
# a={1,2,4,5,4}
# print(type(s))

#-------------------dict---------------------------------------

d={1:100,2:200,3:300}
# d[4]=400
# n=d.fromkeys([1,2],50)
# print(d.get(1))
# print(d.items())
# print(d.keys())
# # d.clear()
# print(d)

# for i in d:
#     print(f"{i}:{d[i]}")

#question---------------------

# a={'a':10,'b':20,'c':20}
# b={'c':30,'d':40}

# for i in b:
#     a[i]=b[i]

# print(a)

# sum=0
# a={'a':10,'b':20,'c':30}
# for i in a :
#     sum+=a[i]
# print(sum)

# a=['a','b','c','c','b','a','a']
# d={}
# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# a={'a':10,'b':20,'c':20}
# b={'c':30,'d':40}
# for i in b:
#     if i in a.keys():
#         a[i]+=b[i]
#     else :
#         a[i]=b[i]
# print(a)

