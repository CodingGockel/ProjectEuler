def fak(n):
    if(n==1):
        return 1
    return n*fak(n-1)
def twentheeth(n):
    k=fak(n)
    sum=0
    for i in str(k):
        sum+=int(i)
    print(sum)
twentheeth(100)