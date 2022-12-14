from collections import defaultdict
from numpy import sign

input_file = open('input/input_day14_1.txt', 'r').read().strip().split('\n')

cave_data = defaultdict(lambda: '.')

for line in input_file:
    coords = [complex(*map(int, pair.split(','))) for pair in line.split(' -> ')]
    for i in range(len(coords) - 1):
        difference = coords[i+1] - coords[i]
        xdiff = int(difference.real)
        ydiff = int(difference.imag)
        if sign(xdiff):
            for dx in range(0, xdiff+sign(xdiff), sign(xdiff)):
                cave_data[coords[i] + dx] = '#'
        if sign(ydiff):
            for dy in range(0, ydiff+sign(ydiff), sign(ydiff)):
                cave_data[coords[i] + dy*1j] = '#'

cave_data[500] = '+'


class Cave:
    def __init__(self, cave_array):
        self.cave_array = cave_array
        self.rock_list = [rock for rock in self.cave_array.keys() if self.cave_array[rock] == '#']
        self.lowest_rock = max(self.rock_list, key=lambda z: z.imag).imag
        self.leftest_rock = min(self.rock_list, key=lambda z: z.real).real
        self.rightest_rock = max(self.rock_list, key=lambda z: z.real).real
        self.sand_position = 500
        self.sand_quantity = 0

    def move_sand(self):
        if self.cave_array[self.sand_position + 1j] == '.':
            self.cave_array[self.sand_position] = '.'
            self.sand_position += 1j
            self.cave_array[self.sand_position] = 'o'
        elif self.cave_array[self.sand_position - 1 + 1j] == '.':
            self.cave_array[self.sand_position] = '.'
            self.sand_position += -1 + 1j
            self.cave_array[self.sand_position] = 'o'
        elif self.cave_array[self.sand_position + 1 + 1j] == '.':
            self.cave_array[self.sand_position] = '.'
            self.sand_position += 1 + 1j
            self.cave_array[self.sand_position] = 'o'
        else:
            self.sand_position = 500
            self.sand_quantity += 1

    def sand_loop(self):
        while (self.sand_position.imag < self.lowest_rock and
                self.leftest_rock <= self.sand_position.real <= self.rightest_rock):
            self.move_sand()
        return self.sand_quantity


cave = Cave(cave_data)

print(cave.sand_loop())




