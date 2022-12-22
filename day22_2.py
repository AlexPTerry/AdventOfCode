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

portals = {
    tuple(x + 1j*-1 for x in range(50, 100)): 'A',
    tuple(x + 1j*-1 for x in range(100, 150)): 'B',
    tuple(150 + 1j*y for y in range(0, 50)): 'C',
    tuple(x + 1j*50 for x in range(100, 150)): 'D',
    tuple(100 + 1j*y for y in range(50, 100)): 'E',
    tuple(100 + 1j*y for y in range(100, 150)): 'F',
    tuple(x + 1j*150 for x in range(50, 100)): 'G',
    tuple(50 + 1j*y for y in range(150, 200)): 'H',
    tuple(x + 1j*200 for x in range(0, 50)): 'I',
    tuple(-1 + 1j*y for y in range(150, 200)): 'J',
    tuple(-1 + 1j*y for y in range(100, 150)): 'K',
    tuple(x + 1j*99 for x in range(0, 50)): 'L',
    tuple(49 + 1j*y for y in range(50, 100)): 'M',
    tuple(49 + 1j*y for y in range(0, 50)): 'N'
}

# Current portal: (Destination, rotation, small => small)
portal_attrs = {
    'A': ('J', 1, True, 3),
    'B': ('I', 0, True, 3),
    'C': ('F', 2, False, 0),
    'D': ('E', 1, True, 1),
    'E': ('D', 3, True, 0),
    'F': ('C', 2, False, 0),
    'G': ('H', 1, True, 1),
    'H': ('G', 3, True, 0),
    'I': ('B', 0, True, 1),
    'J': ('A', 3, True, 2),
    'K': ('N', 2, False, 2),
    'L': ('M', 1, True, 3),
    'M': ('L', 3, True, 2),
    'N': ('K', 2, False, 2),
}


def portal_move(position, dir_index):
    for location_set in portals:
        if position in location_set:
            temp_portal = portals[location_set]
            if dir_index == portal_attrs[temp_portal][3]:
                portal = temp_portal
                location = location_set
                break
    portal_info = portal_attrs[portal]
    dir_index = (dir_index + portal_info[1]) % 4
    for location_set, new_portal in portals.items():
        if new_portal == portal_info[0]:
            new_location = location_set
    if portal_info[2]:
        transport_dict = dict(zip(location, new_location))
    else:
        transport_dict = dict(zip(location, new_location[::-1]))
    new_position = transport_dict[position] + direction_list[dir_index]
    return new_position, dir_index


for movement, rotation in zip(movements, rotations + '_'):
    for _ in range(movement):
        direction = direction_list[direction_index]
        new_direction_index = direction_index
        new_pos = player_pos + direction
        if new_pos in void or new_pos.real > x_max or new_pos.real < 0 or new_pos.imag > y_max or new_pos.imag < 0:
            new_pos, new_direction_index = portal_move(new_pos, new_direction_index)

        if new_pos in wall:
            break
        else:
            player_pos = new_pos
            direction_index = new_direction_index

    if rotation == 'R':
        direction_index = (direction_index + 1) % 4
    elif rotation == 'L':
        direction_index = (direction_index - 1) % 4

print(int(1000*(player_pos.imag+1) + 4*(player_pos.real+1) + direction_index))
