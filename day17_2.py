import numpy as np
from collections import deque


def print_formation(rock_formation):
    arr = np.array([['#' if (i + (rock_max+1-k)*1j) in rock_formation else ' '
                     for i in range(7)] for k in range(rock_max + 2)])
    print(arr)


class Rock:
    def __init__(self, rock_type, start_position):
        self.base_height = start_position.imag
        if rock_type == 1:
            self.rock_positions = np.array([start_position, start_position+1, start_position+2, start_position+3])
            self.edge_positions = np.array([start_position.real, start_position.real+3])
        elif rock_type == 2:
            self.rock_positions = np.array([start_position+1+2j,
                                            start_position+1j, start_position+1+1j, start_position+2+1j,
                                            start_position+1])
            self.edge_positions = np.array([start_position.real, start_position.real+2])
        elif rock_type == 3:
            self.rock_positions = np.array([start_position+2+2j,
                                            start_position+2+1j,
                                            start_position, start_position+1, start_position+2])
            self.edge_positions = np.array([start_position.real, start_position.real+2])
        elif rock_type == 4:
            self.rock_positions = np.array([start_position, start_position+1j, start_position+2j, start_position+3j])
            self.edge_positions = np.array([start_position.real, start_position.real])
        elif rock_type == 5:
            self.rock_positions = np.array([start_position+1j, start_position+1+1j,
                                            start_position, start_position+1])
            self.edge_positions = np.array([start_position.real, start_position.real+1])

    def move_rock(self, direction):
        self.rock_positions += direction
        self.edge_positions += direction.real
        self.base_height += direction.imag

    def jet_rock(self, jet):
        stop = False
        if jet == '<':
            for rock in (self.rock_positions - 1):
                if rock in rock_formation:
                    stop = True
            if self.edge_positions[0] - 1 >= 0 and not stop:
                self.move_rock(-1)
        else:
            for rock in (self.rock_positions + 1):
                if rock in rock_formation:
                    stop = True
            if self.edge_positions[1] + 1 <= 6 and not stop:
                self.move_rock(1)

    def drop_rock(self, rock_formation):
        if self.base_height <= 0:
            return self.rock_positions
        for rock in (self.rock_positions - 1j):
            if rock in rock_formation:
                return self.rock_positions
        self.move_rock(-1j)
        return -1


input_file = open('input/input_day17_1.txt', 'r').read().strip()

rock_formation = set()
active_rock = Rock(1, 2+3j)
num_rocks = 0
i = 0
rock_num = 1
rock_max = -1
rock_max_all = np.array([-1]*7)
old_rock_max = np.array([-1]*7)
past_vals = deque([-1]*100) # <- VERY ARBITRARY NUMBER, NO THOUGHT WENT INTO THIS
past_states = set()

prev_states = {}

while num_rocks < 1000000000000:
    jet = input_file[i]
    active_rock.jet_rock(jet)
    rock_status = active_rock.drop_rock(rock_formation)
    if type(rock_status) != int:
        rock_formation = rock_formation.union(set(rock_status))
        num_rocks += 1
        rock_num = 1 + rock_num % 5
        rock_max = int(max(rock_formation, key=lambda x: x.imag).imag)
        if num_rocks > 100:
            old_rock_max = rock_max
            rock_max_all = np.array([int(max([r for r in rock_formation if r.real == i],
                                         key=lambda x: x.imag).imag) for i in range(7)])
            diff = tuple(rock_max_all - old_rock_max)
            past_vals.popleft()
            past_vals.append(diff)
            tup = (tuple(past_vals), i, rock_num)
            if tup in past_states:
                n_cycle = num_rocks - prev_states[tup][0]       # Length of the cycle
                height_diff = rock_max - prev_states[tup][1]    # Change in rock formation height per cycle
                break
            prev_states[tup] = (num_rocks, rock_max)
            past_states.add(tup)

        active_rock = Rock(rock_num, 2 + rock_max*1j + 4j)
    i = (i+1) % len(input_file)

rock_formation = set()
active_rock = Rock(1, 2+3j)
num_rocks = 0
i = 0
rock_num = 1
rock_max = -1
while num_rocks < (10**12 % n_cycle): # Finds the number of rocks that have fallen before the cycle "starts" such that it ends on 10**12
    jet = input_file[i]
    active_rock.jet_rock(jet)
    rock_status = active_rock.drop_rock(rock_formation)
    if type(rock_status) != int:
        rock_formation = rock_formation.union(set(rock_status))
        num_rocks += 1
        rock_num = 1 + rock_num % 5
        rock_max = int(max(rock_formation, key=lambda x: x.imag).imag)
        active_rock = Rock(rock_num, 2 + rock_max*1j + 4j)

    i = (i+1) % len(input_file)

print(int(max(rock_formation, key=lambda x: x.imag).imag+1) + (10**12 // n_cycle)*height_diff)



