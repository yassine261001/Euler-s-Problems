with open("0022_names.txt") as f:
    names = sorted(f.readline().split(","))

names.insert(0, "")

sums = 0
total = 0

names = [name.strip('"') for name in names]

alphabet = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for name in names:
    for letter in name:
        pos = alphabet.index(letter)
        index = names.index(name)
        nameScore = pos * index
        total += nameScore

print(total)

