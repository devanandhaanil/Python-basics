#palindrome or not
y=int(input("enter your number:"))
x=y
r=0
while x!=0:
    l=x%10
    r=r*10+l
    x=x//10
if r==y:
    print("palindrome")
else:
    print("not palindrome")