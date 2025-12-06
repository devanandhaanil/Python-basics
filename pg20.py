#automorphic number
n=int(input("Enter the number:"))
y=n**2
len=len(str(n))
if y%(10**len)==n:
    print("The number is automorphic")
else:
    print("The number is not automorphic")

