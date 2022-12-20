from collections import deque

input_file = list(map(int, open('input/input_day20_1.txt', 'r').read().strip().split('\n')))
position_list = deque([(811589153*value, index) for index, value in enumerate(input_file)])

for _ in range(10):
    for i, num in enumerate(input_file):
        num = 811589153*num
        current_index = position_list.index((num, i))
        position_list.remove((num, i))
        position_list.rotate(-num)
        position_list.insert(current_index, (num, i))

final_list = list(map(lambda x: x[0], position_list))
zero_index = final_list.index(0)
print(sum(final_list[(zero_index+1000*i) % len(input_file)] for i in [1, 2, 3]))


