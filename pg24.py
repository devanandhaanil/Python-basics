#convert digit of number into words
n=input("Enter the number:")
lst=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
for i in n:
    if i=='-':
        print("Minus",end=' ')
    else:
        print(lst[int(i)],end=' ')

