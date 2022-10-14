def seventh(n):
    primZ=[2]
    i=2
    while len(primZ)<=n+1:
        i+=1
        for z in primZ:
            if i%z==0:
                break
        else:
            primZ.append(i)
    print(primZ)
 
seventh(10001)