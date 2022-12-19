import re


def check_materials(robot, n_materials):
    return all([robot[i] <= n_materials[i] for i in range(3)])


# input_file = open('input/input_day19_1.txt', 'r').read().strip().split('\n')
input_file = open('input/input_test.txt', 'r').read().strip().split('\n')

blueprint_dict = {}
max_depth = 31

for i, line in enumerate(input_file):
    if i > 2:
        break
    params = list(map(int, re.findall(r'\d+', line)))
    blueprint_dict[params[0]] = ((params[1], 0, 0, 0), (params[2], 0, 0, 0),
                                 (params[3], params[4], 0, 0), (params[5], 0, params[6], 0))


def expected_materials(blueprint, material, n_robots, n_materials, depth):
    if material == 0:
        return n_materials[material] + n_robots[material]*(max_depth+1-depth) + (max_depth+1-depth)*(max_depth+2-depth)*0.5

    expected_previous = expected_materials(blueprint, material-1, n_robots, n_materials, depth)
    buildable_robots = int(min(expected_previous // blueprint[material][material-1], max_depth+1-depth))
    return n_materials[material] + n_robots[material]*(max_depth+1-depth) \
        + sum(range(max_depth+2-depth-buildable_robots, max_depth+2-depth))


def search_build(blueprint, n_robots, n_materials, depth, max_geode, path):
    current_state = (tuple(n_robots), tuple(n_materials), depth)
    if depth > max_depth \
            or current_state in state_list\
            or expected_materials(blueprint, 3, n_robots, n_materials, depth) <= max_geode:
        return n_materials[3]
    state_list.add(current_state)
    buildable = reversed([(rtype, robot) for rtype, robot in enumerate(blueprint)
                          if check_materials(robot, n_materials)])

    built_3 = False
    for rtype, robot in buildable:
        next_materials = [n_materials[i] + n_robots[i] - robot[i] for i in range(4)]
        next_robots = n_robots.copy()
        next_robots[rtype] += 1
        new_geode = search_build(blueprint, next_robots, next_materials, depth+1, max_geode, path + [(next_robots, next_materials)])
        max_geode = max(max_geode, new_geode)
        if rtype == 3:
            built_3 = True
            break
    if not built_3:
        n_materials = [n_materials[i] + n_robots[i] for i in range(4)]
    max_geode = max(max_geode, search_build(blueprint, n_robots, n_materials, depth+1, max_geode,
                                            path + [(n_robots, n_materials)]))  # Do nothing
    return max_geode


total_quality = 1
for id, blueprint in blueprint_dict.items():
    state_list = set()
    n_robots = [1, 0, 0, 0]
    n_materials = [0, 0, 0, 0]
    max_geode = search_build(blueprint, n_robots, n_materials, 0, 0, [])
    print(f'{id}: {max_geode}')
    total_quality *= max_geode

print(f'Total quality: {total_quality}')




