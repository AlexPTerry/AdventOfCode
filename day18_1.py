import numpy as np

input_file = open('input/input_day18_1.txt', 'r').read().strip().split('\n')

cube_list = []
for line in input_file:
    cube = list(map(int, line.split(',')))
    cube_list.append(cube)
cube_set = set(map(tuple, cube_list))

total_faces = 0
for cube in cube_set:
    directions = [np.array([0, 0, 1]), np.array([0, 1, 0]), np.array([1, 0, 0]),
                  np.array([0, 0, -1]), np.array([0, -1, 0]), np.array([-1, 0, 0])]

    for direction in directions:
        if tuple(cube + direction) not in cube_set:
            total_faces += 1

print(total_faces)


