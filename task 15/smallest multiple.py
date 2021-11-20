#Smallest multiple
from math import gcd
from functools import reduce
def lcm(a,b):
    return a*b//gcd(a,b)
a=int(input())
for i in range(a):
    b=int(input())
    print(reduce(lcm,range(1,b+1)))
    
    
