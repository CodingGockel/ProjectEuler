
def main(n):
    i=3
    fib1=1
    fib2=1
    while(True):
        help=fib1
        fib1=fib2
        fib2=help+fib2
        if(len(str(fib2))>=n):
            return i
        i+=1
        
print(main(1000))
    

    
        