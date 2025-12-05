#unique characters
n=input("ENTER THE STRING:")
for i in set(n):
    if n.count(i)==1:
       print(i)
