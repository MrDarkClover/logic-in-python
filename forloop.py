# print(range(10,101))
# print(range(23,57))
# print(range(0,47,2))

# for i in range(101,0,-20):
#     print(i)

# n= 12
# for i in range(1,11):
#     print(n*i)

# S="Student"
# for i in range(len(S)):
#     print(f"{i} : {S[i]}")

# for i in range(1,11):
#     if i == 3:
#         continue
#         print(i)
#     if i == 11:
#         break
#     print(i)
# else:
#     print("no break")

# n=int(input("enter num: "))
# for i in range(n+1):
#     print("hello world")

# n=int(input("enter num: "))
# for i in range(1,n+1):
#     print(i)

# n=int(input("enter num: "))
# for i in range(n,0,-1):
#     print(i)

# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")

# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# f=1
# for i in range(1,n+1):
#     f*=i
# print(f)

# even=odd=0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         even+=i
#     else:
#         odd+=i
# print(f"even: {even},odd: {odd}")

# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)

# out=int(input("Enter output: "))
# sum=0
# for i in range(1,n):
#     if n % i == 0:
#         sum+=i
# print(sum)
# if out == sum:
#     print(f"{sum}=={out}")
# else:
#     print("error")

# count=0
# for i in range(1,n+1):
#     if n % i == 0:
#         count+=1   
# if count == 2 :
#     print("it is prime num")
# else:
#     print("it is not a primes")

# rev=""
# s= "student"
# for i in range(len(s)-1,-1,-1):
#     rev+=s[i]
# print(rev)
# print(s[::-1])

# palin=""
# S="maam"
# for i in range(len(S)-1,-1,-1):
#     palin+=S[i]
# if S == palin:
#     print("palindrome")
# else:
#     print("not palindrome")

# S="1234HiHello@"
# dc=0
# lc=0
# SCc=0
# for i in S:
#     if i.isdigit():
#         dc+=1
#     elif i .isalpha():
#         lc+=1
#     else:
#         SCc+=1
# print(f"{dc},   {lc},   {SCc}")


# --------------------------------While LOOP--------------------------------------------------------------------

# a=54321
# while a != 0:
#     lst = a % 10
#     print(lst)
#     a//=10

# rev=0
# a=54321
# while a != 0:
#     lst = a % 10
#     rev=rev*10+lst
#     a//=10
# print(rev)

# p=0
# s=a=1124
# while a != 0:
#     p=p*10+a%10
#     a//=10
# if s == p:
#     print("palindrome")
# else: 
#     print("not")
