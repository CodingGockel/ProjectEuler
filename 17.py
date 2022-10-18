import inflect

def seventhteenth(n):
    p=inflect.engine()
    sum=0
    for i in range(1,n+1):
        w=p.number_to_words(i)
        w=w.replace(" ","").replace("-","")
        print(w)
        sum+=len(w)
    print(sum)
seventhteenth(1000)