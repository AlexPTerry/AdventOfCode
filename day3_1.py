
input_file = open('input/input_day3_1.txt', 'r')

total = 0
for line in input_file:
    n = len(line) - 1
    line1 = line[:n//2]
    line2 = line[n//2:n]

    character = set(line1).intersection(line2).pop()
    value = ord(character) - ord('A') + 27 if character.isupper() else ord(character) - ord('a') + 1
    total += value

print(total)