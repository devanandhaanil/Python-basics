#armstrong number or not
n = int(input("Enter a number: "))
ans=0
x=n
while x!=0:
    ans=ans+((x%10)**3)
    x=x//10
if ans==n:
    print("armstrong")
else:
    print("not a armstrong")


