import re


def m_dist(z1, z2):
    return int(abs(z1.real - z2.real) + abs(z1.imag - z2.imag))


input_file = open('input/input_day15_1.txt', 'r').read().strip().split('\n')

blocked_positions = set()
yline = 2000000
for n in range(len(input_file)):
    line = input_file[n]
    line_numbers = list(map(int, re.findall(r'\d+', line)))
    sensor_position = line_numbers[0] + 1j*line_numbers[1]
    beacon_position = line_numbers[2] + 1j*line_numbers[3]
    distance = m_dist(sensor_position, beacon_position)
    dy = int(yline - sensor_position.imag)
    abs_dy = abs(dy)

    if abs_dy <= distance:
        for i in range(-(distance-abs_dy), distance-abs_dy+1):
            blocked_position = sensor_position+i+dy*1j
            if blocked_position != beacon_position:
                blocked_positions.add(blocked_position)

print(len(blocked_positions))



