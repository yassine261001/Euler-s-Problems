def SumSquareDiff():

    sumOfSquares = 0
    numsSum = 0
    squareOfSums = 0

    for i in range(1,101):
        sumOfSquares += i**2

    for i in range(1,101):
        numsSum += i
        squareOfSums = numsSum**2

    difference = squareOfSums - sumOfSquares

    return difference

print(SumSquareDiff())

