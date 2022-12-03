
input_file = open('input/input_day3_1.txt', 'r')

total = 0
n = 0
elf = []
for line in input_file:
    n += 1
    elf.append(set(line[:len(line)-1]))
    if n == 3:
        n = 0
        character = elf[0].intersection(elf[1]).intersection(elf[2]).pop()
        value = ord(character) - ord('A') + 27 if character.isupper() else ord(character) - ord('a') + 1
        elf = []
        total += value

print(total)
