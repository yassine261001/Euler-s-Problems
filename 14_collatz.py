def findMax():
    
    max_len = 0
    best_start = 0

    for start in range(2, 1000000):
        n = start
        sequence_len = 1

        while n != 1:

            if n % 2 != 0:
                n = 3 * n + 1

            else:
                n = n // 2
            sequence_len += 1

        if sequence_len > max_len:
            max_len = sequence_len
            best_start = start

    print(f"Starting number: {best_start}")
    print(f"Length: {max_len}")

findMax()

