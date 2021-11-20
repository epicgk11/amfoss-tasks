lis = input("")
developer = list(map(int , input("").split()))
developer.sort()
probsol = list(map(int , input("").split()))
probsol.sort()
overpo=[]
for i in probsol:
    for j in developer:
        if i > j:
            overpo.append(i)
            developer.remove(j)
            break
        if i < j:
            continue
if len(overpo) < len(developer):
    print("NO")
    exit()
else :
    power = 0
    for i in  overpo:
        power +=i
    print("YES")
    print(power)
