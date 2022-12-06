
def findDivs(n):
    l=[]
    for i in range (1,int(n//2)+1):
        if(n%i==0):
            l.append(i)
    return l

def allAbundant(n):
    l=[]
    for i in range(12,n+1):
        sum=0
        k=findDivs(i)
        for e in k:
            sum+=e
        if(sum>i):
            l.append(i)
    return l

def main(n):
    sum=0
    allAbs=allAbundant(n)
    allSums=[]
    for e in allAbs:
        for k in allAbs:
            if(e+k<=n):
                allSums.append(e+k)
            else:
                break
    for i in range(1,n+1):
        if(not(i in allSums)):
            sum+=i
    return sum

print(main(28123))

