def main(n):
    sum=0
    i=1
    for i in range(2,500000):
        if(sumDigitsToPowerOfFive(i,n)==i):
            sum+=i
    return sum
def sumDigitsToPowerOfFive(i,n):
    sum=0
    for e in str(i):
        sum+=int(e)**n
    return sum

print(main(5))
