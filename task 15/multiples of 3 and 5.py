#multiples of 3 and 5
N=int(input())
for i in range(N):
    s=0
    a=int(input())
    for j in range(a):
        if j%3==0 or j%5==0:
            s=s+j
    print(s)
