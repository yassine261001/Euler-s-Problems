def is_palindrome():
    palindrome = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            for z in range(100, 1000):
                result = x*y*z
                strResult = str(result)
                if strResult == strResult[::-1]:
                    intResult = int(strResult)
                    palindrome = max(palindrome, intResult)
    return palindrome

print(is_palindrome())

