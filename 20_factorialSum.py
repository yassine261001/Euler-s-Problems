def factorial():
    
    n = int(input("Enter a random number: "))
    result = n
    numSum = 0

    for i in range(1, n):
        result *= i

    for char in str(result):
        numSum += int(char)

    return numSum

print(factorial())

