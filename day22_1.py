import re

input_file = open('input/input_day22_1.txt', 'r').read().strip('\n').split('\n\n')

input_grid = input_file[0].split('\n')
directions = input_file[1]

void = {x+1j*y for x in range(max(len(line) for line in input_grid)) for y in range(len(input_grid))}
wall = set()
ground = set()
tractable = set()
grid = []

for y, line in enumerate(input_grid):
    for x, char in enumerate(line):
        if char != ' ':
            tractable.add(x+1j*y)
            void.remove(x+1j*y)
            grid.append((x, y))
        if char == '#':
            wall.add(x+1j*y)
        elif char == '.':
            ground.add(x+1j*y)

x_max = max(point[0] for point in grid)
y_max = max(point[1] for point in grid)
x_range = {y: [-1, -1] for y in range(y_max+1)}
y_range = {x: [-1, -1] for x in range(x_max+1)}

for x, y in grid:
    if (x - 1) + 1j*y in void or x - 1 < 0:
        x_range[y][0] = x
    if (x + 1) + 1j*y in void or x + 1 > x_max:
        x_range[y][1] = x
    if x + 1j*(y - 1) in void or y - 1 < 0:
        y_range[x][0] = y
    if x + 1j*(y + 1) in void or y + 1 > y_max:
        y_range[x][1] = y

movements = map(int, re.findall(r'\d+', directions))
rotations = re.sub(r'[0-9]+', '', directions)

player_pos = x_range[0][0] + 1j*0

direction_list = [1, 1j, -1, -1j]
direction_index = 0

for movement, rotation in zip(movements, rotations + '_'):
    for _ in range(movement):
        direction = direction_list[direction_index]
        new_pos = player_pos + direction
        if new_pos in void or new_pos.real > x_max or new_pos.real < 0 or new_pos.imag > y_max or new_pos.imag < 0:
            if direction.imag == 0:
                current_range = x_range[new_pos.imag]
                modulo = current_range[1] - current_range[0] + 1
                new_pos = (new_pos.real - current_range[0]) % modulo + current_range[0] + 1j*new_pos.imag
            else:
                current_range = y_range[new_pos.real]
                modulo = current_range[1] - current_range[0] + 1
                new_pos = new_pos.real + 1j*((new_pos.imag - current_range[0]) % modulo + current_range[0])

        if new_pos in wall:
            break
        else:
            player_pos = new_pos

    if rotation == 'R':
        direction_index = (direction_index + 1) % 4
    elif rotation == 'L':
        direction_index = (direction_index - 1) % 4

print(int(1000*(player_pos.imag+1) + 4*(player_pos.real+1) + direction_index))
