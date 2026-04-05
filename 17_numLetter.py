underTwenty = [
    "", "one", "two",
    "three", "four", "five",
    "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve",
    "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen",
    "nineteen"
    ]

overTwenty = [
    "", "ten", "twenty", "thirty", "forty", "fifty", "sixty",
    "seventy", "eighty", "ninety"
    ]

suffixes = [
    "", "hundred", "thousand", "million", "billion"
    ]


def convert_number():
    num = input("Enter a number from 0 to 1000: ")
    
    
    if int(num) == 0:
        word = "zero"
        return word

    if int(num) < 20:
        word = underTwenty[int(num)]
        return word
    
    if int(num) >= 20 and int(num) % 10 == 0 and int(num) < 100:
        num = int(num) // 10
        word = overTwenty[num]
        return word

    if int(num) > 20 and int(num) < 100:
        first = int(num[1])
        second = int(num[0])

        word = overTwenty[second] + " " + underTwenty[first]
        return word

    if int(num) >= 100 and int(num) <= 999:
        first = int(num[2])
        second = int(num[1])
        third = int(num[0])

        if second == 0 and first == 0:
            word = underTwenty[third] + " " + suffixes[1]
            return word

        if second == 1:
            first = int(num[2]) + 10
            word = underTwenty[third] + " " + suffixes[1] + " and " + underTwenty[first]
            return word

        if second == 0:
            word = underTwenty[third] + " " + suffixes[1] + " and " + underTwenty[first]
            return word

        if first == 0:
            word = underTwenty[third] + " " + suffixes[1] + " and " + overTwenty[second]
            return word
        else:
            word = underTwenty[third] + " " + suffixes[1] + " and " + overTwenty[second] + " " + underTwenty[first]
            return word

    if int(num) == 1000:
        first = int(num[3])
        second = int(num[2])
        third = int(num[1])
        fourth = int(num[0])

        word = underTwenty[fourth] + " " + suffixes[2]
        return word
    

print(convert_number())

