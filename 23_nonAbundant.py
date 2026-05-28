def getDivisors(n):
    divisors = []

    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


def classify_numbers(limit):
    perfect = []
    abundant = []
    deficient = []

    for n in range(1, limit+1):
        divisors = getDivisors(n)
        s = sum(divisors)

        if s == n:
            perfect.append(n)

        elif s > n:
            abundant.append(n)

        elif s < n:
            deficient.append(n)
    
    return perfect, abundant, deficient

perfect, abundant, deficient = classify_numbers(28123)


abundant_sums = set()

for x in abundant:
    for y in abundant:
        if x + y <= 28123:
            abundant_sums.add(x + y)

result = 0

for i in range(1, 28124):
    if i not in abundant_sums:
        result += i

print(result)



