import re
from collections import defaultdict

input_file = open('input/input_day16_1.txt', 'r').read().strip().split('\n')

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
    if flow_rate > 0:
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

print(len(valuable_valves))




