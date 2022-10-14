def fourth():
    palins=[]
    for i in range (1,1000):
        for k in range (1,1000):
            z=i*k
            if str(z)==str(z)[::-1]:
                palins.append(z)
    palins.sort()
    print(palins[-1])
fourth()