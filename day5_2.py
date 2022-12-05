from collections import deque

input_lines = open('input/input_day5_1.txt', 'r').readlines()

line_break = 0
temp_stack = deque([])
for i in range(len(input_lines)):
    line = input_lines[i]

    if line == '\n':
        line_break = i
        num_stacks = (len(input_lines[line_break-1]) + 1) // 4
        stack_list = [deque([]) for i in range(num_stacks)]
        for j in range(line_break-2, -1, -1):
            for k in range(num_stacks):
                if len(input_lines[j]) > k*4+1:
                    block = input_lines[j][k*4+1]
                    if block != ' ':
                        stack_list[k].append(input_lines[j][k*4+1])

    elif line_break:
        line_split = line.split()
        i_move = int(line_split[1])
        i_from = int(line_split[3])
        i_to = int(line_split[5])

        for j in range(i_move):
            temp_stack.append(stack_list[i_from-1].pop())
        for j in range(i_move):
            stack_list[i_to-1].append(temp_stack.pop())

top_crates = ''.join([stack.pop() for stack in stack_list])

print(top_crates)
# print(stack_list)

