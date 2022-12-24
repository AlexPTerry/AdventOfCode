from collections import deque, defaultdict
from math import lcm

input_file = open('input/input_day24_1.txt', 'r').read().strip().split('\n')

len(input_file), len(input_file[0])

x_len = len(input_file[0])
y_len = len(input_file)

repeat = lcm(x_len-2, y_len-2)

player_position_true = 1+1j*0
end_position_true = (x_len-2)+1j*(y_len-1)
player_movement = [1, -1, 1j, -1j, 0]

grid = {i+1j*k for i in range(1, x_len-1) for k in range(1, y_len-1)} | {player_position_true, end_position_true}

directions = {'>': 1, 'v': 1, '<': -1, '^': -1}
wind_cardinal_initial = {'>': set(), 'v': set(), '<': set(), '^': set()}
for k, line in enumerate(input_file):
    for i, char in enumerate(line):
        if char in {'>', 'v', '<', '^'}:
            wind_cardinal_initial[char].add(i+1j*k)

wind_positions_initial = set.union(*wind_cardinal_initial.values())


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


wind_position_dict = {0: wind_cardinal_initial}
next_wind_cardinal_initial = wind_cardinal_initial
for i in range(1, 600):
    next_wind_cardinal_initial = move_wind(next_wind_cardinal_initial)
    wind_position_dict[i] = next_wind_cardinal_initial


def move_player(initial_player_position, end_position, initial_wind_cardinal, initial_depth):
    S = deque([])
    S.append((initial_player_position, initial_wind_cardinal, initial_depth))
    state_set = set()
    state_dict = {}

    while len(S) > 0:
        player_position, wind_cardinal, depth = S.popleft()

        state = (player_position, depth % repeat)
        if player_position == end_position:
            return depth, state, state_dict, wind_cardinal

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


final_depth0, end_state0, state_dict0, wind_cardinal0 = move_player(player_position_true,
                                                                    end_position_true, wind_cardinal_initial, 0)

# Lazily copying and pasting code!
wind_position_dict = {0: wind_cardinal0}
next_wind_cardinal_initial = wind_cardinal0
for i in range(1, 600):
    next_wind_cardinal_initial = move_wind(next_wind_cardinal_initial)
    wind_position_dict[i] = next_wind_cardinal_initial
final_depth1, end_state1, state_dict1, wind_cardinal1 = move_player(end_position_true,
                                                                    player_position_true, wind_cardinal0, 0)

wind_position_dict = {0: wind_cardinal1}
next_wind_cardinal_initial = wind_cardinal1
for i in range(1, 600):
    next_wind_cardinal_initial = move_wind(next_wind_cardinal_initial)
    wind_position_dict[i] = next_wind_cardinal_initial
final_depth2, end_state2, state_dict2, wind_cardinal2 = move_player(player_position_true,
                                                                    end_position_true, wind_cardinal1, 0)


print(f'{final_depth0} + {final_depth1} + {final_depth2} = {final_depth0+final_depth1+final_depth2}')








