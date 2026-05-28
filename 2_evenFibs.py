def fibonacci(n):

    sequence = [0,1]
    sumEven = 0

    while sequence[-1] + sequence[-2] <= n:
        sequence.append(sequence[-1] + sequence[-2])

    for i in sequence:
        if i % 2 == 0:
            sumEven += i
    return sumEven

print(fibonacci(4000000))

