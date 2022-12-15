import re


def m_dist(z1, z2):
    return int(abs(z1.real - z2.real) + abs(z1.imag - z2.imag))


input_file = open('input/input_day15_1.txt', 'r').read().strip().split('\n')
yline = 2000000

blocked_positions = set()
beacon_positions = set()
blocked_frames = []
for n in range(len(input_file)):
    line = input_file[n]
    line_numbers = list(map(int, re.findall(r'\d+', line)))
    sensor_position = line_numbers[0] + 1j*line_numbers[1]
    beacon_position = line_numbers[2] + 1j*line_numbers[3]
    distance = m_dist(sensor_position, beacon_position)
    dy = int(yline - sensor_position.imag)
    abs_dy = abs(dy)

    if beacon_position.imag == yline:
        beacon_positions.add(beacon_position)

    if abs_dy <= distance:
        new_frame = [sensor_position.real - (distance-abs_dy), sensor_position.real + (distance-abs_dy)]
        added = True
        while added:
            added = False
            for frame in blocked_frames:
                if (new_frame[0] <= frame[0] <= new_frame[1]
                        or new_frame[0] <= frame[1] <= new_frame[1]
                        or frame[0] <= new_frame[0] <= frame[1]
                        or frame[0] <= new_frame[1] <= frame[1]):
                    blocked_frames.remove(frame)
                    new_frame = [min(new_frame[0], frame[0]), max(new_frame[1], frame[1])]
                    added = True
                    break
            if not added:
                blocked_frames.append(new_frame)

total_length = sum([frame[1] - frame[0] + 1 for frame in blocked_frames]) - len(beacon_positions)
print(int(total_length))



