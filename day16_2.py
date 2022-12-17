import re
from collections import defaultdict, deque
from copy import deepcopy

input_file = open('input/input_day16_1.txt', 'r').read().strip().split('\n')
start_valve = 'AA'
max_time = 26
time_open = 1

adjacent_valves = {}
valve_flow_rates = {}

valuable_valves = set()

for line in input_file:
    current_valve = line.split()[1]
    flow_rate = int(re.search(r'\d+', line).group())

    if 'valves ' in line:
        linked_valves = line.split('valves ')[1].split(', ')
    else:
        linked_valves = [line.split('valve ')[1]]

    adjacent_valves[current_valve] = linked_valves
    valve_flow_rates[current_valve] = flow_rate
    if flow_rate > 0 or current_valve == start_valve:
        valuable_valves.add(current_valve)


class Dijkstra:
    def __init__(self, unvisited, start_node, end_nodes, node_map):
        self.unvisited = unvisited
        self.visited = set()
        self.start_node = start_node
        self.end_nodes = end_nodes
        self.node_map = node_map
        self.node_distance = {valve: 999 for valve in unvisited}
        self.node_distance[start_node] = 0

    def visit_node(self, current_node):
        for node in self.node_map[current_node]:
            if node not in self.visited:
                if self.node_distance[current_node] + 1 < self.node_distance[node]:
                    self.node_distance[node] = self.node_distance[current_node] + 1
        self.unvisited.remove(current_node)
        self.visited.add(current_node)

    def run_dijkstras(self):
        while not self.end_nodes.issubset(self.visited):
            current_node = min(self.unvisited, key=self.node_distance.get)
            self.visit_node(current_node)
        return {node: self.node_distance[node] for node in self.end_nodes}


valve_distances = {}
for valve in valuable_valves:
    valve_dijkstra = Dijkstra(list(valve_flow_rates.keys()), valve, valuable_valves, adjacent_valves)
    valve_distances[valve] = valve_dijkstra.run_dijkstras()


location = deque([])
path_dict = defaultdict(lambda: -1)


def travel(current_valve, current_time, unvisited_valves, score):
    end = True
    location.append(current_valve)

    valves_sorted = sorted(unvisited_valves, key=valve_distances[current_valve].get)

    for next_valve in valves_sorted:
        next_time = current_time - valve_distances[current_valve][next_valve] - time_open
        if next_time < 0:
            break
        next_unvisited_valves = [valve for valve in deepcopy(unvisited_valves) if valve != next_valve]
        next_score = score + next_time*valve_flow_rates[next_valve]
        travel(next_valve, next_time, next_unvisited_valves, next_score)
        end = False
    path_dict[tuple(sorted(list(location)))] = max(score, path_dict[tuple(sorted(list(location)))])
    location.pop()


travel(start_valve, max_time, valuable_valves, 0)
sorted_vals = sorted([(key, path_dict[key]) for key in path_dict.keys()], key=lambda x: x[1], reverse=True)


def check_disjoint(t1, t2):
    return set(t1[0][1:]).isdisjoint(set(t2[0][1:]))


total_combinations = len(sorted_vals)
best_two = sorted([((sorted_vals[i][0], sorted_vals[j][0]), sorted_vals[i][1] + sorted_vals[j][1])
                   for i in range(total_combinations) for j in range(total_combinations)
                   if check_disjoint(sorted_vals[i], sorted_vals[j])], key=lambda x: x[1], reverse=True)

print(best_two[0])

