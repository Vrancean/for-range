m=int(input("dati m:"))
s=0
for i in range(1,m):
    if (i%3==0) and (i%5==0):
        s+=i
print("suma =",s)