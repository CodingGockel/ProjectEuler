import math
def main(n):
    l=[]
    for a in range (2,n+1):
        for b in range (2,n+1):
            num=a**b
            if(not(num in l)):
                l.append(num)
    return len(l)
print(main(100))
                