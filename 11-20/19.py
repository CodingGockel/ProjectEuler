import math

def istSchaltjahr(a):
    if ((a%4)==0 or (a%400)==0) and (a%100!=0):
        return True
    return False
def ninetheen(y):
    sunns=0
    d=0
    u=2
    for i in range(1901,y):
        for j in range(1,13):
            if(j==4 or j==6 or j==9 or j==11):
                d=30
            elif(j==2):
                if(istSchaltjahr(i)):
                    d=29
                else:
                    d=28
            else:
                d=31
            for k in range(1,d+1):
                if(u==7 and k==1):
                    sunns+=1
                if(u==7):
                    u=1
                else:
                    u+=1
    print(sunns)
ninetheen(2001)