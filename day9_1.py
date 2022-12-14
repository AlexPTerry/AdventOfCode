from numpy import sign


def move_t(h, t):
    y_dist = h[0] - t[0]
    x_dist = h[1] - t[1]

    if y_dist ** 2 + x_dist ** 2 > 2:
        t[0] += sign(y_dist)
        t[1] += sign(x_dist)

    return [t[0], t[1]]


input_file = open('input/input_day9_1.txt', 'r').read().strip().split('\n')

h_pos = [0, 0]
t_pos = [0, 0]

t_history = {tuple(t_pos)}

for line in input_file:
    vector = line.split(' ')
    direction = 0 if vector[0] in ['U', 'D'] else 1
    distance = int(vector[1]) if vector[0] in ['U', 'R'] else -int(vector[1])

    for _ in range(abs(distance)):
        h_pos[direction] += sign(distance)
        t_pos = move_t(h_pos, t_pos)
        t_history.add(tuple(t_pos))


print(len(t_history))

