def findLargestPrimeFactor(n):
  primeFactor = 1
  i = 2

  while i <= n / i:
    if n % i == 0:
      primeFactor = i
      n /= i
    else:
      i += 1

  if primeFactor < n: primeFactor = int(n)

  return primeFactor
a=int(input())
for i in range(a):
    b=int(input())
    print(findLargestPrimeFactor(b))
