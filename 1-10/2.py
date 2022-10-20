def second():
    i=1
    k=1
    sum=0
    fib=0
    while fib<=4000000:
        fib= i+k
        if fib%2==0:
            sum+=fib
        i=k
        k=fib
    print(sum)

second()