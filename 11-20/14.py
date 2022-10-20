import math
import sys
def genchain(n,k):
    if(n==1):
        return k
    if(n%2==0):
        return genchain(n/2,k+1)
    else:
        return genchain(3*n+1,k+1)
def fourtheen(n):
    l=0
    y=0
    for i in range(1,n):
        z=genchain(i,1)
        if(z>l):
            l=z
            y=i
    print(y)
class recursion_depth:
    def __init__(self, limit):
        self.limit = limit
        self.default_limit = sys.getrecursionlimit()
    def __enter__(self):
        sys.setrecursionlimit(self.limit)
    def __exit__(self, type, value, traceback):
        sys.setrecursionlimit(self.default_limit)

sys.setrecursionlimit(2000000)
fourtheen(1000000)
sys.setrecursionlimit(1000)