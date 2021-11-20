#Amfoss praveshanam program 2
def Q2(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    print((len(l)))
n=int(input())
Q2(n)
