import re
from collections import defaultdict, deque
from copy import deepcopy

input_file = open('input/input_day16_1.txt', 'r').read().strip().split('\n')
start_valve = 'AA'
max_time = 30 - 4
time_open = 1

# input_file = open('input/input_test.txt', 'r').read().strip().split('\n')
# start_valve = 'AA'
# max_time = 30 - 4
# time_open = 1

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


def travel(c_valve, ce_valve, r_time, re_time, c_flow, max_flow, c_valuable_valves, path, epath):
    # print(path, r_time, c_flow)
    true_values = {}
    for n_valve in c_valuable_valves:
        expected_flow = (r_time - valve_distances[c_valve][n_valve] - time_open)*valve_flow_rates[n_valve]
        true_values[n_valve] = expected_flow
    valve_order = sorted(true_values.keys(), key=true_values.get, reverse=True)
    max_i = -1
    for i in range(min(len(valve_order), 16)):
        n_flow = c_flow
        if r_time >= re_time:
            n_valve = valve_order[i]
            ne_valve = ce_valve
            if r_time - time_open < valve_distances[c_valve][n_valve]:
                break
            else:
                n_valuable_valves = deepcopy(c_valuable_valves)
                n_valuable_valves.remove(n_valve)
                n_flow += (r_time - valve_distances[c_valve][n_valve] - time_open) * valve_flow_rates[n_valve]
            n_max_flow = travel(n_valve, ne_valve,
                                        r_time - valve_distances[c_valve][n_valve] - time_open,
                                        re_time,
                                        n_flow, max_flow, n_valuable_valves, path + [n_valve], epath)
        else:
            n_valve = c_valve
            ne_valve = valve_order[i]
            if re_time - time_open < valve_distances[c_valve][ne_valve]:
                break
            else:
                n_valuable_valves = deepcopy(c_valuable_valves)
                n_valuable_valves.remove(ne_valve)
                n_flow += (re_time - valve_distances[ce_valve][ne_valve] - time_open) * valve_flow_rates[ne_valve]
            n_max_flow = travel(n_valve, ne_valve,
                                        r_time,
                                        re_time - valve_distances[ce_valve][ne_valve] - time_open,
                                        n_flow, max_flow, n_valuable_valves, path, epath + [ne_valve])
        max_flow = max(n_max_flow, max_flow)
        if max_flow == n_max_flow:
            max_i = i

    if max_i == -1:
        return c_flow
    return max(c_flow, max_flow)


# for key in valuable_valves:
#     print(key, ':', valve_distances[key])
#
# print({key: valve_flow_rates[key] for key in valuable_valves})
print(travel(start_valve, start_valve, max_time, max_time, 0, 0, valuable_valves, [start_valve], [start_valve]))



