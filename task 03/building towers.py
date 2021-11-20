import statistics
from statistics import mode

#Amfoss building towers
N=int(input())
L=[]

#constraint checked
if N>=1000 and N<=1:
    print("constraint not followed")

#adding to a list

L =list(map(int,input().split()))

#final output operations
l3=list(set(L))

print(L.count(mode(L)),len(l3),end=' ')

    
