from collections import defaultdict, deque

input_file = open('input/input_day23_1.txt', 'r').read().strip().split('\n')
# input_file = open('input/input_test.txt', 'r').read().strip().split('\n')

elf_set = set()

for y, line in enumerate(input_file):
    for x, char in enumerate(line):
        if char == '#':
            elf_set.add(x + 1j*y)

n_directions = ({i + -1j for i in [-1, 0, 1]}, -1j)
s_directions = ({i + 1j for i in [-1, 0, 1]}, 1j)
w_directions = ({-1 + 1j*i for i in [-1, 0, 1]}, -1)
e_directions = ({1 + 1j*i for i in [-1, 0, 1]}, 1)

directions_list = deque([n_directions, s_directions, w_directions, e_directions])

all_directions = n_directions[0] | s_directions[0] | w_directions[0] | e_directions[0]

round_num = 0
elf_move = True
while elf_move:
    elf_move = False
    elf_copy = set()
    position_dict = defaultdict(lambda: 0)
    proposition_dict = {}
    for elf in elf_set:
        surrounding_positions = set(elf + direction for direction in all_directions)
        if not surrounding_positions & elf_set:
            elf_copy.add(elf)
            position_dict[elf] += 1
            continue

        proposed = False
        for x_direction, movement in directions_list:
            if not {elf + direction for direction in x_direction} & elf_set:
                position_dict[elf + movement] += 1
                proposition_dict[elf] = elf + movement
                proposed = True
                break

        if not proposed:
            elf_copy.add(elf)
            position_dict[elf] += 1

    for elf, proposition in proposition_dict.items():
        if position_dict[proposition] == 1:
            elf_copy.add(proposition)
            elf_move = True
        else:
            elf_copy.add(elf)

    elf_set = elf_copy.copy()
    directions_list.rotate(-1)
    round_num += 1
    if round_num > 9:
        break

x_min = min(elf.real for elf in elf_set)
x_max = max(elf.real for elf in elf_set)
y_min = min(elf.imag for elf in elf_set)
y_max = max(elf.imag for elf in elf_set)

print(int((x_max - x_min + 1)*(y_max - y_min + 1) - len(elf_set)))
















