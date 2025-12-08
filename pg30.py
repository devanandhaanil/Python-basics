# find duplicates in list
ls= [1,2,3,2,4,3]
l1=[]
for i in ls:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')