#move all zeroes towards the end
n = [2,0,4,3,7,0,5,6,0,7]
non_zeros = []
zeros = []
for i in n:
    if i!= 0:
        non_zeros.append(i)
    else:
        zeros.append(i)
result = non_zeros + zeros
print(result)
