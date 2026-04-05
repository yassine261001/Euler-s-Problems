def findPrimes(n):
    s = [True] * (n+1)
    s[0] = s[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            for j in range(i*i, n+1, i):
                s[j] = False

    primes = [i for i in range(n+1) if s[i]]
    return sum(primes)

print(findPrimes(2000000))

