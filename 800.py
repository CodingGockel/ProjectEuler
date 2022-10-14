def last(n):
    solutions=0
    l=[]
    """
    for i in range (1,int(Decimal(n).sqrt())):
        for k in range (1,int(Decimal(n).sqrt())):
            if i!=k:
                z= i**k * k**i
                if z==n:
                    solutions+=1
                    l.append([i,k])
                    print(solutions,l)
    print("Lösungen:{0}\n Terme:{1}".format(solutions,l))
    
    
    for i in range (1,int(Decimal(n).sqrt())):
        for k in range (1,int(Decimal(n).sqrt())):
            z= i**k * k**i
            if z<n:
                if i!=k:
                    if z==n:
                        solutions+=1
                        l.append([i,k])
                        print(solutions,l)
            else:
                break
    print("Lösungen:{0}\n Terme:{1}".format(solutions,l))
    
    i=0
    k=0
    z=(i**k) * (k**i)
    while z<=n:
        i+=1
        k=1
        z=(i**k) * (k**i)
        while z<=n:
            k+=1
            z=(i**k) * (k**i)
            if i!=k:
                if z==n:
                    solutions+=1
                    l.append([i,k])
                    print(solutions,l)
    """
    q=0
    nMax=n
    for i in range (2,nMax):
        z= i**2 * 2**i
        if(z>n):
            break
        for k in range (2,n):
            z= i**k * k**i
            print(i,k)
            if z>n:
                if nMax==n:
                    nMax=k-1
                break
            if i!=k:
                if z==n:
                    solutions+=1
                    l.append([i,k])
                    #l.append([k,i])
                    #print(solutions,l)
                    break
    print("Lösungen:{0}\n Terme:{1}".format(solutions,l))
last(800)