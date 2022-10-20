def fith():
    i=10
    z=True
    while z:
        for k in range (1,21):
            if i%k==0:
                if k==20:
                    z=False
                    print(i)
            else:
                break
        i+=10

fith()