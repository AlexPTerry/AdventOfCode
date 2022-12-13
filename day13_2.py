import ast
from functools import cmp_to_key


def compare_lists(list1, list2):
    if type(list1) != type(list2):
        if type(list1) == int:
            return compare_lists([list1], list2)
        else:
            return compare_lists(list1, [list2])
    elif type(list1) == int:
        if list1 < list2:
            return -1
        elif list1 == list2:
            return 0
        else:
            return 1
    else:
        for i in range(min(len(list1), len(list2))):
            if list1[i] == list2[i]:
                pass
            else:
                return compare_lists(list1[i], list2[i])
        if len(list1) < len(list2):
            return -1
        elif len(list1) == len(list2):
            return 0
        else:
            return 1


input_file = open('input/input_day13_1.txt', 'r').read().strip().split('\n\n')

packet_list = [[[2]], [[6]]]
for i in range(len(input_file)):
    pair = input_file[i].split('\n')
    packet1 = ast.literal_eval(pair[0])
    packet2 = ast.literal_eval(pair[1])

    packet_list.append(packet1)
    packet_list.append(packet2)

cmp_key = cmp_to_key(compare_lists)
packet_list.sort(key=cmp_key)

print((packet_list.index([[2]]) + 1) * (packet_list.index([[6]]) + 1))
