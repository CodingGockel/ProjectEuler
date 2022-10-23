import time

def generateDivisors(curIndex, curDivisor, arr):
    if (curIndex == len(arr)):
        print(curDivisor, end = ' ')
        return
     
    for i in range(arr[curIndex][0] + 1):
        generateDivisors(curIndex + 1, curDivisor, arr)
        curDivisor *= arr[curIndex][1]

def normal(n):
    l=[] 
    for i in range(1, n//2 +1): 
        if n % i==0: 
            l.append(i) 
    l.append(n) 
    return(l)

def primfactorization(n):
    arr = []
    i = 2
    while(i * i <= n):
        if (n % i == 0):
            count = 0
            while (n % i == 0):
                n //= i
                count += 1
            arr.append([count, i])
    if (n > 1):
        arr.append([1, n])
    curIndex = 0
    curDivisor = 1
    generateDivisors(curIndex, curDivisor, arr)
    
"""
normal_time = time.time()
normal(10000)
print("--- %s seconds with normal ---" % (time.time() - normal_time))
normal_time= time.time()
primfactorization(10)
print("--- %s seconds with primfactorisation ---" % (time.time() - normal_time))
"""
def sumOfDivs(n):
    l=0 
    for i in range(1, n//2 +1): 
        if n % i==0: 
            l+=i 
    return l

def thirtheen(n):
    sum=0
    for i in range (1,n+1):
        sims=sumOfDivs(i)
        if(sims!=i):
            if(i==sumOfDivs(sims)):
                sum+=i
    return sum

print(thirtheen(10000))