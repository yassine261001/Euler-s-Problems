amicable = []

for n in range(1, 10000):
    firstSum = 0
    secondSum = 0

    for i in range(1, n):
        if n % i == 0:
            firstSum += i

    for i in range(1, firstSum):
        if firstSum % i == 0:
            secondSum += i

    if n == secondSum and n < firstSum:
        amicable.append(n)
        amicable.append(firstSum)

        print(f"{n} and {firstSum} are amicable numbers.")

print(amicable)

print(sum(amicable))

