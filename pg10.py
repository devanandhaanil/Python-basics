#perfect square
n=int(input("Enter no:"))
ls=[]
for i in range(1,n):
    if n%i==0:
        ls.append(i)
x=sum(ls)
if x==n:
    print("perfect square")
else:
    print("not perfect square")