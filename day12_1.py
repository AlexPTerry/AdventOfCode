

input_file = open('input/input_day12_1.txt', 'r').read().strip().split('\n')

height_map = []
start_pos = []
end_pos = []
unvisited_nodes = []
visited_nodes = []
travel_dict = dict()

width = len(input_file[0])
height = len(input_file)

for i in range(height):
    line = input_file[i]
    height_line = []
    for j in range(width):
        char = line[j]
        if char == 'S':
            start_pos = (i, j)
            char = 'a'
        elif char == 'E':
            end_pos = (i, j)
            char = 'z'

        height_line.append(ord(char) - ord('a'))
        unvisited_nodes.append((i, j))
    height_map.append(height_line)

for i in range(height):
    for j in range(width):
        visitable_nodes = []
        for m in [-1, 0, 1]:
            for n in [-1, 0, 1]:
                if 0 <= i+m < height and 0 <= j+n < width and abs(n)+abs(m) == 1:
                    if height_map[i+m][j+n] - height_map[i][j] <= 1:
                        visitable_nodes.append((i+m, j+n))
        travel_dict[(i, j)] = visitable_nodes


class Dijkstra:
    def __init__(self, unvisited, visited, start_node, end_node, node_map):
        self.unvisited = unvisited
        self.visited = visited
        self.start_node = start_node
        self.end_node = end_node
        self.node_map = node_map
        self.node_distance = dict(zip(unvisited_nodes, [999]*(height*width)))
        self.node_distance[start_node] = 0

    def visit_node(self, current_node):
        for node in self.node_map[current_node]:
            if node not in self.visited:
                if self.node_distance[current_node] + 1 < self.node_distance[node]:
                    self.node_distance[node] = self.node_distance[current_node] + 1
        self.unvisited.remove(current_node)
        self.visited.append(current_node)

    def run_dijkstras(self):
        while self.end_node not in self.visited:
            current_node = min(self.unvisited, key=self.node_distance.get)
            self.visit_node(current_node)
        return self.node_distance[self.end_node]


graph = Dijkstra(unvisited_nodes, visited_nodes, start_pos, end_pos, travel_dict)
print(graph.run_dijkstras())
