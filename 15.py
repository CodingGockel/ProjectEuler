import math
import sys
def fifthteen(n):
    sys.setrecursionlimit(2000000)
    y=(fak(n*2))/(fak(n)*fak(n))
    print(int(y))
    sys.setrecursionlimit(1000)
def fak(n):
    if(n==1):
        return 1
    return n*fak(n-1)
fifthteen(20)