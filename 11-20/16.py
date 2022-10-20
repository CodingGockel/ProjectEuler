def sixteenth(n):
    sum=0
    s=str(n)
    for i in s:
        sum+=int(i)
    print(sum)

sixteenth(2**1000)