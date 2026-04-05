def primes(n):
    found = []
    i = 2
    while len(found) < n:
        is_multiple = False

        for p in found:
            if i % p == 0:
                is_multiple = True
                break

        if not is_multiple:
            found.append(i)
        i +=1

    return found

result = primes(10001)
print(result[-1])

