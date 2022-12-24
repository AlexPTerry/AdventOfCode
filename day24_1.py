from collections import deque, defaultdict

input_file = open('input/input_day24_1.txt', 'r').read().strip().split('\n')
# input_file = open('input/input_test.txt', 'r').read().strip().split('\n')

len(input_file), len(input_file[0])

x_len = len(input_file[0])
y_len = len(input_file)

player_position = 1+1j*0
end_position = (x_len-2)+1j*(y_len-1)
player_movement = [1, -1, 1j, -1j, 0]

grid = {i+1j*k for i in range(1, x_len) for k in range(1, y_len)} | {player_position, end_position}

directions = {'>': (1, 1), 'v': (1, 1), '<': (-1, 1), '^': (-1, 1)}
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
        direction = directions[key][0]
        offset = directions[key][1]
        modulo = (x_len-2) if key in {'>', '<'} else (y_len-2)
        for wind in value:
            direction = directions[key][0]
            offset = directions[key][1]
            if key in {'>', '<'}:
                updated_wind.add((wind.real - offset + direction) % modulo + offset + 1j*wind.imag)
            else:
                updated_wind.add(wind.real + 1j*((wind.imag - offset + direction) % modulo + offset))

        updated_wind_cardinal[key] = updated_wind
    return updated_wind_cardinal


def move_player(initial_player_position, initial_wind_cardinal, initial_depth):
    S = deque([])
    S.append((initial_player_position, initial_wind_cardinal, initial_depth))
    min_depth = 99999
    state_set = set()
    state_dict = {}
    min_distance = 999999

    while len(S) > 0:
        player_position, wind_cardinal, depth = S.popleft()

        old_wind_positions = set.union(*wind_cardinal.values())
        old_state = (player_position, tuple(frozenset(winds) for winds in wind_cardinal.values()))
        if player_position == end_position:
            return depth, state_dict, state

        next_wind_cardinal = move_wind(wind_cardinal)
        wind_positions = set.union(*next_wind_cardinal.values())

        potential_positions = list(({player_position + z for z in player_movement} & grid) - wind_positions)
        potential_positions.sort(key=lambda z: abs(z.real-end_position.real) + abs(z.imag - end_position.imag))
        if len(potential_positions) > 0:
            z = potential_positions[0]
            dist = abs(z.real - end_position.real) + abs(z.imag - end_position.imag)
            if dist < min_distance:
                print(dist)
                min_distance = dist
        # print(depth, len(potential_positions), [len(value) for value in wind_cardinal.values()])

        # if depth+1 < 500:
        for i, position in enumerate(potential_positions):
            state = (position, tuple(frozenset(winds) for winds in next_wind_cardinal.values()))
            if state not in state_set:
                state_set.add(state)
                S.append((position, next_wind_cardinal, depth+1))
                state_dict[state] = old_state


final_depth, state_dict, end_state = move_player(player_position, wind_cardinal, 0)

print(final_depth, end_state)

# state_path = []
# current_state = end_state
#
# for i in range(final_depth):
#     state_path.append(current_state)
#     current_state = state_dict[current_state]

# for state in state_path[::-1]:
#     print(state)

# value_dict = defaultdict(lambda: 0)
# for value in state_dict.values():
#     for key in state_dict:
#         if state_dict[key] == value:
#             value_dict[value] += 1


# print([(value) for key, value in value_dict.items() if value > 1])




# import numpy as np
# print(wind_positions)
# print(x_len, y_len)
# wind_grid = np.array([['.' for i in range(x_len)] for j in range(y_len)], dtype=object)
#
# for _ in range(12):
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
#     print()
#
#     wind_cardinal = move_wind(wind_cardinal)







