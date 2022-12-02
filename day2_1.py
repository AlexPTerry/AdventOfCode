
input_file = open('input/input_day2_1.txt', 'r')

value_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

score = 0
for line in input_file:
    score += value_dict[line[2]] + ((value_dict[line[2]] - value_dict[line[0]] + 1) % 3) * 3

print(score)
