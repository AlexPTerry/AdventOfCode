import ast


def compare_lists(list1, list2):
    if type(list1) != type(list2):
        if type(list1) == int:
            return compare_lists([list1], list2)
        else:
            return compare_lists(list1, [list2])
    elif type(list1) == int:
        return list1 <= list2
    else:
        for i in range(min(len(list1), len(list2))):
            if list1[i] == list2[i]:
                pass
            else:
                return compare_lists(list1[i], list2[i])
        return len(list1) <= len(list2)


input_file = open('input/input_day13_1.txt', 'r').read().strip().split('\n\n')

total = 0
for i in range(len(input_file)):
    pair = input_file[i].split('\n')
    packet1 = ast.literal_eval(pair[0])
    packet2 = ast.literal_eval(pair[1])

    if compare_lists(packet1, packet2):
        total += i + 1

print(total)


