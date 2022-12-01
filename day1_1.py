
input_file = open('input/input_day1_1.txt', 'r')

max_calories = 0
current_calories = 0
for line in input_file:
    if line != '\n':
        current_calories = current_calories + int(line)
    else:
        max_calories = max(max_calories, current_calories)
        current_calories = 0

max_calories = max(max_calories, current_calories)
print(max_calories)
