#q1
lis = list(map(int,input().split()))
a=lis[0]
b=lis[1]
t1=0
t2=0
t3=0

n= []
while a % 2 == 0:
    t1=t1+1
    a=a/2
for i in range(1,b + 1):
    t3 = 0
    j = i
    while j % 2 == 0:
        j=j/ 2
        t3=t3+1
    if t3 < t1:
        t2=t2+1
        n.append(int(i))

print(t2)
for i in n:
    print(i,end=' ')
