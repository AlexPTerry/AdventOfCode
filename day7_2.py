
input_file = open('input/input_day7_1.txt', 'r')
# input_file = open('input/input_test.txt', 'r')

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

if listing:
    file_dict[c_dir] = concat_array
    concat_array = []
    listing = False

size_dict = dict()
def sum_sizes(key):
    key_size = 0
    for e in file_dict[key]:
        if e[0] == 'dir':
            key_size = key_size + sum_sizes(key + (e[1],))
        else:
            key_size = key_size + int(e[0])
    size_dict[key] = key_size
    return key_size


sum_sizes(('/',))
space_to_clear = size_dict[('/',)] - 40000000
print(min([val for val in size_dict.values() if val > space_to_clear]))