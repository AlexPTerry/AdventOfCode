from collections import deque, defaultdict
from math import lcm

input_file = open('input/input_day24_1.txt', 'r').read().strip().split('\n')

len(input_file), len(input_file[0])

x_len = len(input_file[0])
y_len = len(input_file)

repeat = lcm(x_len-2, y_len-2)

player_position = 1+1j*0
end_position = (x_len-2)+1j*(y_len-1)
player_movement = [1, -1, 1j, -1j, 0]

grid = {i+1j*k for i in range(1, x_len-1) for k in range(1, y_len-1)} | {player_position, end_position}

directions = {'>': 1, 'v': 1, '<': -1, '^': -1}
wind_cardinal = {'>': set(), 'v': set(), '<': set(), '^': set()}
for k, line in enumerate(input_file):
    for i, char in enumerate(line):
        if char in {'>', 'v', '<', '^'}:
            wind_cardinal[char].add(i+1j*k)

wind_positions = set.union(*wind_cardinal.values())


def move_wind(wind_cardinal):
    updated_wind_cardinal = {}
    for key, value in wind_cardinal.items():
        updated_wind = set()
        modulo = (x_len-2) if key in {'>', '<'} else (y_len-2)
        for wind in value:
            direction = directions[key]
            if key in {'>', '<'}:
                updated_wind.add((wind.real - 1 + direction) % modulo + 1 + 1j*wind.imag)
            else:
                updated_wind.add(wind.real + 1j*((wind.imag - 1 + direction) % modulo + 1))

        updated_wind_cardinal[key] = updated_wind
    return updated_wind_cardinal


wind_position_dict = {0: wind_cardinal}
next_wind_cardinal = wind_cardinal
for i in range(1, 600):
    next_wind_cardinal = move_wind(next_wind_cardinal)
    wind_position_dict[i] = next_wind_cardinal


def move_player(initial_player_position, initial_wind_cardinal, initial_depth):
    S = deque([])
    S.append((initial_player_position, initial_wind_cardinal, initial_depth))
    state_set = set()
    state_dict = {}

    while len(S) > 0:
        player_position, wind_cardinal, depth = S.popleft()

        state = (player_position, depth % repeat)
        if player_position == end_position:
            return depth, state, state_dict

        next_wind_cardinal = wind_position_dict[(depth+1) % repeat]
        next_wind_positions = set.union(*next_wind_cardinal.values())

        potential_positions = list(({player_position + z for z in player_movement} & grid) - next_wind_positions)
        potential_positions.sort(key=lambda z: abs(z.real-end_position.real) + abs(z.imag - end_position.imag))

        for i, next_position in enumerate(potential_positions):
            next_state = (next_position, (depth+1) % repeat)
            if next_state not in state_set:
                state_set.add(next_state)
                S.append((next_position, next_wind_cardinal, depth+1))
                state_dict[next_state] = state


final_depth, end_state, state_dict = move_player(player_position, wind_cardinal, 0)
print(final_depth, end_state)

# Testing stuff below

# current_state = end_state
# state_path = [current_state]
#
# for i in range(final_depth):
#     current_state = state_dict[current_state]
#     state_path.append(current_state)
#
# for state in state_path[::-1]:
#     print(state)
#
#
# import numpy as np
# wind_grid = np.array([['.' for i in range(x_len)] for j in range(y_len)], dtype=object)
#
# for i in range(final_depth+1):
#     print(i)
#     wind_grid = np.array([['.' for i in range(x_len)] for j in range(y_len)], dtype=object)
#     for y, line in enumerate(wind_grid):
#         for x, char in enumerate(line):
#             if x + 1j*y in wind_cardinal['>']:
#                 wind_grid[y][x] = '>'
#             elif x + 1j*y in wind_cardinal['v']:
#                 wind_grid[y][x] = 'v'
#             elif x + 1j*y in wind_cardinal['<']:
#                 wind_grid[y][x] = '<'
#             elif x + 1j*y in wind_cardinal['^']:
#                 wind_grid[y][x] = '^'
#     for line in wind_grid:
#         print(''.join(line))
#
#     wind_cardinal = move_wind(wind_cardinal)







