
def move_t(h, t):
    y_dist = h[0] - t[0]
    x_dist = h[1] - t[1]

    if abs(y_dist) > 1:
        t[0] += y_dist // abs(y_dist)
        if abs(x_dist) > 0:
            t[1] += x_dist // abs(x_dist)
    if abs(x_dist) > 1:
        t[1] += x_dist // abs(x_dist)
        if abs(y_dist) > 0:
            t[0] += y_dist // abs(y_dist)

    return [t[0], t[1]]


input_file = open('input/input_day9_1.txt', 'r').read().strip().split('\n')
# input_file = open('input/input_test.txt', 'r').read().strip().split('\n')

h_pos = [0, 0]
t_pos = [0, 0]

t_history = {tuple(t_pos)}

for line in input_file:
    vector = line.split(' ')
    direction = 0 if vector[1] in ['U', 'D'] else 1
    distance = int(vector[1]) if vector[0] in ['U', 'R'] else -int(vector[1])

    for _ in range(abs(distance)):
        # print('H:', h_pos, 'T:', t_pos, 'Dist', distance, 'Line:', line)
        h_pos[direction] += distance // abs(distance)
        t_pos = move_t(h_pos, t_pos)
        t_history.add(tuple(t_pos))

print('H:', h_pos, 'T:', t_pos, 'Dist', distance, 'Line:', line)

print(len(t_history))
# print(t_history)

