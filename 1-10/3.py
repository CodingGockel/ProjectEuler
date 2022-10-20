import math
def findPrimzahl(z):
    for i in range (2,int(math.sqrt(z))):
        if z%i==0:
            return i
    return z
def third(n):
    z=n
    l=[]
    while z>1:
        p=findPrimzahl(z)
        l.append(p)
        z=z//p
    return l

print(third(600851475143))