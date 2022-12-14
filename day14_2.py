from collections import defaultdict
from numpy import sign

input_file = open('input/input_day14_1.txt', 'r').read().strip().split('\n')
# input_file = open('input/input_test.txt', 'r').read().strip().split('\n')

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


class Cave:
    def __init__(self, cave_array):
        self.cave_array = cave_array
        self.rock_list = [rock for rock in self.cave_array.keys() if self.cave_array[rock] == '#']
        self.lowest_rock = max(self.rock_list, key=lambda z: z.imag).imag
        self.leftest_rock = min(self.rock_list, key=lambda z: z.real).real
        self.rightest_rock = max(self.rock_list, key=lambda z: z.real).real
        self.sand_position = 500
        self.sand_quantity = 0
        self.max_sand_height = 500

    def move_sand(self):
        if self.sand_position.imag + 1 == self.lowest_rock + 2:
            self.max_sand_height = min(self.max_sand_height, self.sand_position.imag)
            self.sand_position = 500
            self.cave_array[self.sand_position] = 'o'
            self.sand_quantity += 1
        elif self.cave_array[self.sand_position + 1j] == '.':
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
            self.max_sand_height = min(self.max_sand_height, self.sand_position.imag)
            self.sand_position = 500
            self.sand_quantity += 1
            self.cave_array[self.sand_position] = 'o'

    def sand_loop(self):
        while '.' in [self.cave_array[500], self.cave_array[500+1j], self.cave_array[499+1j], self.cave_array[501+1j]]:
            self.move_sand()
        return self.sand_quantity + 1


cave = Cave(cave_data)

print(cave.sand_loop())

# Cave printer!
# for y in range(0, int(cave.lowest_rock)+2):
#     for x in range(300, 700):
#         print(cave.cave_array[x + y*1j], end='')
#     print()




