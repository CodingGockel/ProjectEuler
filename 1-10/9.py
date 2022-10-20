def ninth(n):
    for c in range (3,n):
        for b in range (1,c):
            for a in range (0,b):
                z=a**2+b**2
                if z==c**2:
                    y=a+b+c
                    if y==n:
                        print("a:"+str(a)+"\n"+"b:"+str(b)+"\n"+"c:"+str(c)+"\n")
                        print(a*b*c)
                        return True

ninth(1000)