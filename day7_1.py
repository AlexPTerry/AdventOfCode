
input_file = open('input/input_day7_1.txt', 'r')

c_dir = ()

file_dict = dict()
listing = False
concat_array = []

for line_raw in input_file:
    line = line_raw.strip()
    if line[0] == '$':
        if listing:
            file_dict[c_dir] = concat_array
            concat_array = []
            listing = False
        if line[2:4] == 'cd':
            new_dir = line[5:]
            if new_dir == '..':
                c_dir = tuple(c_dir[:-1])
            elif c_dir == '/':
                c_dir = ('/',)
            else:
                c_dir = c_dir + (line[5:],)
        elif line[2:4] == 'ls':
            listing = True
    elif listing:
        concat_array.append(tuple(line.split(' ')))


print(file_dict)