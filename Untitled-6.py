n=int(input("Dati n= "))
x=1
y=0
s1=0
s2=0
s3=0
s4=0
s5=0
z=1
q=0
for x in range(1,n+1,1):
    y=x+y
print("Raspunsul= ", y)

n=int(input("Dati n= "))
for x in range(1,n+1,1):
    s1=((x-1)*x)+s1
print("Raspunsul= ", s1)

n=int(input("Dati n= "))
for x in range(1,n+1,1):
    z*=x
    s2+=z
print("Raspunsul= ", s2)

n=int(input("Dati n= "))
for x in range(1,n+1,1):
    x=str(x)
    x=int(x+"2")
    s3=s3+x
print("Raspunsul= ", s3)

n=int(input("Dati n= "))
for x in range(1,n+1,1):
    q=x/(x+1)
    s4=s4+q
print("Raspunsul= ", s4)

n=int(input("Dati n= "))
for x in range(1,n+1,1):
    x=str(x)
    x=int("2"+x)
    s5=s5+x
print("Raspunsul= ", s5)