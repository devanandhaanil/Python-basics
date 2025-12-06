#to find prime factors of numbers
def prime_factors(num):
  f = []
  factor = 2
  while (num >= 2):
    if (num % factor == 0):
      f.append(factor)
      num = num / factor
    else:
      factor += 1
  return f
n=int(input(" Enter the number to find the factorial of: "))
print(set((prime_factors(n))))

