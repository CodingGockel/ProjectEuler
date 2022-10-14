def sixth():
    sumOfSquares=0
    squareSum=0 
    for i in range (1,101):
        sumOfSquares= sumOfSquares+i**2
    for i in range (1,101):
        squareSum= squareSum+i
    squareSum=squareSum**2
    print(sumOfSquares)
    print(squareSum-sumOfSquares)     
    
sixth()