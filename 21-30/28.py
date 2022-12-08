import math
def main(n):
    sum=1
    u=n*n
    k=1
    while (u>1):
        for i in range (4):
            sum+=u
            u-=n-k
        k+=2
    return sum
print(main(1001))
    
    