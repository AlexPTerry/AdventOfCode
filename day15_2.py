import re


def m_dist(z1, z2):
    return int(abs(z1.real - z2.real) + abs(z1.imag - z2.imag))


input_file = open('input/input_day15_1.txt', 'r').read().strip().split('\n')
max_search_x = 4000000
max_search_y = 4000000

for yline in range(max_search_y):
    blocked_positions = set()
    blocked_frames = []
    for n in range(len(input_file)):
        line = input_file[n]
        line_numbers = list(map(int, re.findall(r'\d+', line)))
        sensor_position = line_numbers[0] + 1j*line_numbers[1]
        beacon_position = line_numbers[2] + 1j*line_numbers[3]
        distance = m_dist(sensor_position, beacon_position)
        dy = int(yline - sensor_position.imag)
        abs_dy = abs(dy)

        if abs_dy <= distance:
            new_frame = [max(0, sensor_position.real - (distance-abs_dy)),
                         min(max_search_x, sensor_position.real + (distance-abs_dy))]
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

    total_length = sum([frame[1] - frame[0] + 1 for frame in blocked_frames])
    if total_length <= max_search_x:
        x_pos = blocked_frames[0][1]+1
        print(int(yline + max_search_x*x_pos))
        break


