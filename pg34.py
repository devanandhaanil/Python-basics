#find all subsets
n= [1,2]
subsets = [[]]
for i in n:
    size = len(subsets)
    for j in range(size):
        subsets.append(subsets[j] + [i])
print(subsets)

