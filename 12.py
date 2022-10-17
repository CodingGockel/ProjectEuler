import math
def twelv(n):
    number=0
    i=1
    while(numberOfDiv(number)<n):
        number+=i
        i+=1
    print(number)
def numberOfDiv(n):
    nod=0
    sqrt=int(math.sqrt(n))
    for i in range (1,sqrt+1):
        if(n%i==0):
            nod+=2
    if sqrt*sqrt==0:
       nod-=1 
    return nod
twelv(500)