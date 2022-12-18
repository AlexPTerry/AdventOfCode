import numpy as np
import sys
from collections import defaultdict, deque

input_file = open('input/input_day18_1.txt', 'r').read().strip().split('\n')
# input_file = open('input/input_test.txt', 'r').read().strip().split('\n')

cube_list = []
for line in input_file:
    cube = list(map(int, line.split(',')))
    cube_list.append(cube)
cube_set = set(map(tuple, cube_list))

directions = [np.array([0, 0, 1]), np.array([0, 1, 0]), np.array([1, 0, 0]),
              np.array([0, 0, -1]), np.array([0, -1, 0]), np.array([-1, 0, 0])]

total_faces = 0
air_count = defaultdict(lambda: 0)
air_set = set()
for cube in cube_set:
    for direction in directions:
        air_location = tuple(cube + direction)
        if air_location not in cube_set:
            total_faces += 1
            air_set.add(air_location)
            air_count[air_location] += 1


def maxi(clist):
    tmax = np.array([-1]*3)
    for c in clist:
        tmax = np.maximum(tmax, c)
    return tmax

def mini(clist):
    tmin = np.array([99999]*3)
    for c in clist:
        tmin = np.minimum(tmin, c)
    return np.array(tmin)


max_dimensions = maxi(cube_list) + 1
min_dimensions = mini(cube_list) - 1

def in_volume(cube):
    return all(min_dimensions <= cube) and all(cube <= max_dimensions)


start_pos = max_dimensions
filled = set()
Q = deque([])


def flood_fill(pos):
    filled.add(tuple(pos))
    Q.append(tuple(pos))
    while len(Q) > 0:
        pos = Q.pop()
        for direction in directions:
            new_pos = pos + direction
            if in_volume(new_pos) and tuple(new_pos) not in cube_set.union(filled):
                filled.add(tuple(new_pos))
                Q.append(tuple(new_pos))


flood_fill(start_pos)

not_filled = set([(i, j, k) for i in range(min_dimensions[0], max_dimensions[0]+1)
                  for j in range(min_dimensions[1], max_dimensions[1]+1)
                  for k in range(min_dimensions[2], max_dimensions[2]+1)]) - cube_set - filled

dry_sides = 0
for air in not_filled:
    dry_sides += air_count[air]

print(total_faces - dry_sides)

