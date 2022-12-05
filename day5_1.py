from collections import deque

input_lines = open('input/input_day5_1.txt', 'r').readlines()

line_break = 0
for i in range(len(input_lines)):
    line = input_lines[i];

    if line == '\n':
        line_break = i
        num_stacks = (len(input_lines[line_break-1]) + 1) // 2
        stack_list = [deque([]) for i in range(num_stacks)]
        for j in range(line_break-2, -1, -1):
            for k in range(num_stacks):
                stack_list[k].append(input_lines[j][k*2])

    #if line_break:
        # DO STUFF

print(stack_list)

