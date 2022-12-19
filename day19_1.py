import re


def check_materials(robot, n_materials):
    return all([robot[i] <= n_materials[i] for i in range(3)])

input_file = open('input/input_day19_1.txt', 'r').read().strip().split('\n')

blueprint_dict = {}

for line in input_file:
    params = list(map(int, re.findall(r'\d+', line)))
    blueprint_dict[params[0]] = ((params[1], 0, 0), (params[2], 0, 0),
                                 (params[3], params[4], 0), (params[5], 0, params[6]))


def search_build(blueprint, n_robots, n_materials, depth):
    if depth > 24:
        return n_materials[3]
    n_materials = [n_materials[i] + n_robots[i] for i in range(4)]
    buildable = [robot for robot in blueprint if check_materials(robot)]
    max_obsidian = -1
    for r_type, robot in buildable:
        next_materials = [n_materials[i] - robot[i] for i in range(3)]
        next_robots = n_robots.copy()
        next_robots[r_type] += 1
        max_obsidian = max(max_obsidian, search_build(blueprint, next_robots, next_materials, depth+1))
    max_obsidian = max(max_obsidian, search_build(blueprint, n_robots, n_materials, depth+1))  # Do nothing
    return max_obsidian


for id, blueprint in blueprint_dict.items():
    n_robots = [1, 0, 0, 0]
    n_materials = [0, 0, 0, 0]
    print(f'{id}: {search_build(blueprint, n_robots, n_materials, 0)}')




