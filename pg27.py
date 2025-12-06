#sum of digits of a number
a=int(input("Enter the number: "))
sum=0
n=a
while n!=0:
    x=n%10
    sum=sum+x
    n=n//10
print(sum)