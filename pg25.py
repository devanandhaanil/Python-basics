#factorial using recursion
def factorial(n):
   if n==0 or n==1:
       return 1
   else:
       return n*factorial(n-1)

n=int(input(" Enter the number to find the factorial of: "))
print(factorial(n))