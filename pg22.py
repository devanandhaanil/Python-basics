#find smallest element in list
ls=[2,4,7,1,5,9]
for i in set(ls):
    ls.sort()
print(ls[0])