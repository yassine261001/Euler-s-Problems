def fibonacci():
    a = 0
    b = 1
    index = 1
 
    while len(str(b)) < 1000:
        c = a + b
        a = b
        b = c
        index += 1
    return b, index

print(fibonacci())