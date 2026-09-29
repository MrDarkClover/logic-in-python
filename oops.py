#---------------------------------class------------------
# class Car:
#     a= 12
#     def hello():
#         print("hello world")

# print(Car.a)
# Car.hello()

# class Bags:
#     name ="dark"
#     def de(self):
#         print("details")

# c=Bags()
# print(c.name)
# c.de()

#----------------------------constructor---------------
# class cal:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

# C=cal(2,5)
# print(C.a)

#----------------------------Attributes and Methods----------------------

# class ani:
#     a=12
#     def __init__(self,name):
#         self.name=name
#     def hello(self):
#         print("how are you")

# o=ani("mice")

#---------------------------------inheritance------------------------------
# class animal:
#     def __init__(self,name):
#         self.name=name

# class lion(animal):
#     pass

# o=lion("Raj")
# print(o.name)


# class factory:
#     def __init__(self,material,zips,pockets):
#         self.material=material
#         self.zips= zips
#         self.pockets=pockets

#     def printdet(self):
#         print("details:")
#         print(self.material)
#         print(self.zips)
#         print(self.pockets)

# class reebok(factory):
#     def __init__(self, material, zips, pockets,color):
#         super().__init__(material, zips, pockets)
#         self.color=color

#     def printdet(self):
#         print(self.color)
#         return super().printdet()

# class perfect(reebok):
#     def __init__(self, material, zips, pockets, color):
#         super().__init__(material, zips, pockets, color)
#     def printdet(self):
#         return super().printdet()
    
# bag1= factory("leather",5,10)
# bag2= reebok("leather",3,7,"black")
# bag3= perfect("nilon",2,7,"pink")

# bag3.printdet()
# bag1.printdet()

# --------------------polymorphism--------------------------------------

# def hello():
#     print("how")

# def hello():
#     print("what")

# hello()
 
#method overriding(we need inheritance)

#-------------------------------- encapsulation-------------------------------------

# class add:
#     __a=12

# class sub(add):
#     print(add.__a)
    
# o=sub()
# print(o.a)

#----------------------------abstraction-----------------------------------------------------

#------------------Dunder method--------------------------------

# class Ani:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return f"hello {self.name}"
# o=Ani("vikas")
# print(o)
    
# class cal:
#     def __init__(self,num):
#         self.num=num
#     def __add__(self, other):
#         return self.num+other.num
#     def __eq__(self, value):
#         return self.num == value.num
# n1=cal(30)
# n2=cal(30)
# print(n1+n2)
# print(n1==n2)

# ----------------------------- args, kwargs ---------------------------------------

# def add(*args):
#     return args

# print(add(20,30))

# def info(**kwargs):
#     return kwargs

# print(info(name="om",age="20",id="101"))

# ------------------------------- one liner -------------------------------------------------
# a=20
# print("even") if a%2 == 0 else print("odd")

# a=[1,2,3,4,5,6,7,8,9,0]
# b=[i for i in a if i%2==0]
# print(b)

#---------------------------lambda--------------------------------
# check=lambda x: print("even") if x%2==0 else print("odd")
# check(12)

# -----------------------map,filter,zip---------------------------

# a=["om","vikas","raghav","raj"]
# # for i in a:
# #     print(len(i))

# lengths=list(map(len,a))
# print(lengths)

# temp_cel=[20,30,50,44]

# def convert(a):
#     far =(a * 9/5)+32
#     return far

# for i in temp_cel:
#     print(convert(i))

# temp_far =list(map(lambda x : (x*9/5 + 32),temp_cel))
# print(temp_far)

# -------------filter----------------

# m=[35,80,80,12,60,49]

# passed=list(filter(lambda x: x>= 40,m))
# print(passed)

#---------------zip---------------------------------------------------------------------
# name = ['om','vikas','raj','mama']
# marks=[12,90,42,6,33]

# res=list(zip(name,marks))
# print(res)

#----------------------------------------------------------------------------------
