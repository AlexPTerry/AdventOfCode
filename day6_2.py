
input_lines = open('input/input_day6_1.txt', 'r')

char_queue = 14*['-1']
i = 0
for c in input_lines.read():
    i += 1
    char_queue = char_queue[1:] + [c]
    char_no = [char_queue.count(char_i)-1 for char_i in char_queue]
    if not any(char_no) and i > 14:
        break

print(i)
