#find longest palindrome and its length
ls= ["dood", "cac", "took", "malayalam", "Zooooooyza", "LOOOOOOOOOOOL"]
max=0
for i in ls:
    if i.lower()[::-1]==i.lower():
        l=len(i)
        if l>max:
            max=l
print(max)