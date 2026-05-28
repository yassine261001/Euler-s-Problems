from itertools import permutations
import math

#version 1

perm = permutations([0, 1,2,3,4,5,6,7,8,9])

lex = []

for i in perm:
    lex.append(i)

print(len(lex))
print(lex[999999])

# version 2

digits = [0,1,2,3,4,5,6,7,8,9]
n = 999_999
result = []

for i in range(9, -1, -1):
    fact = math.factorial(i)
    idx = n // fact
    result.append(digits[idx])
    digits.pop(idx)
    n %= fact

    print(fact, idx)
    

print("".join(map(str, result)))

