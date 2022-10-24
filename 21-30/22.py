def pos(l):
    return ord(l.lower()) - 96

def writeSorted():
    #does not work
    o = open(r"C:\Users\Admin\Desktop\GitHubProjects\ProjectEuler\21-30\p022_names.txt", "r")
    z=o.read()
    o.close()
    l=z.replace('"',"").split(",")
    for e in l:
        e.replace(" ","")
    y=1
    for i in range (0,len(l)):
        for j in range (0,len(l)-y):
            k=0
            if(len(l[j])>len(l[j+1])):
                k=len(l[j+1])
            else:
                k=len(l[j])
            for e in range (0,k):
                if(l[j][e]>l[j+1][e]):
                    h=l[j]
                    l[j]=l[j+1]
                    l[j+1]=h
                    break
                elif(l[j][e]==l[j+1][e]):
                    continue
                else:
                    break
        y+=1
    f = open(r"./21-30/sorted.txt", "w")
    f.write(str(l).replace("[","").replace("]",""))
    f.close()
def twenthetwo(q):
    f= open(q, "r")
    z= f.read()
    l=z.replace("'","").replace(" ","").replace('"',"").split(",")
    l.sort()
    total=0
    for j in range(0,len(l)):
        sum=0
        for i in l[j]:
            sum+=pos(i)
        total+= (sum)*(j+1)
    print(total)
    
#writeSorted()
#twenthetwo(r"21-30\p022_names.txt")
twenthetwo(r"21-30\p022_names.txt")