pl=[]
for i in range(100,1000):
    for j in range(100,1000):
        a = i * j
        if str(a) == str(a)[::-1]:
            pl.append(a)
pl.sort()
l=len(pl)
n=int(input())
for p in range(n):
    a = int(input())
    for i in range(l-1,-1,-1):
        if pl[i]<a:
            print(pl[i])
            break
