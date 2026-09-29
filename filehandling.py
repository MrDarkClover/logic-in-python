# open("new.txt","x")

# f=open("in.txt",'w')
# d=input("write some data : ")
# f.write(d)
# f.close()

# f=open('in.txt','r')
# print(f.read())
# f.close()

with open('in.txt','a') as f:
    f.write(" "+"check")
