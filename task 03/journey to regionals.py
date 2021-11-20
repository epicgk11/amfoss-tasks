import string
#hackerrank praveshanam jorney to regionals
N=int(input())
List=list(map(int,input().split()))
a=int(input())
p=[]

for i in range(a):
    l2=list(map(int,input().split()))
    p.append(l2)
s=0

for i in p:
    d=i[1]
    a=i[0]
    for u in range(a-1,d):
        try:
            s=s+List[u]
        except:
            continue
    print(s)
    
    s=0
