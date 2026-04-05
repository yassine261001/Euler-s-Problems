result = 0
num = 1
divisors = 0

while divisors < 500:
    result += num
    num += 1

    divisors = 0

    for i in range(1, result+1): 
        if i*i > result:
            break
        if result % i == 0:
            divisors += 2
            if i * i == result:
                divisors -= 1
    
print(f"Result: {result}")
print(f"Divisors: {divisors}")


