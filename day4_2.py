from operator import add

input_file = open('input/input_day4_1.txt', 'r')

i = 0
for line in input_file:
    elf_range = line.split(',')
    elf_list = [set(range(*map(add, [int(e) for e in r.split('-')], [0, 1]))) for r in elf_range]
    intersection = elf_list[0] & elf_list[1]
    if len(intersection) > 0:
        i += 1

print(i)



