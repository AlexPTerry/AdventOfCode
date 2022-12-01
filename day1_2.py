
input_file = open('input/input_day1_1.txt', 'r')

max_calories = [0, 0, 0]
current_calories = 0
for line in input_file:
    if line != '\n':
        current_calories = current_calories + int(line)
    else:
        max_calories[0] = max(max_calories[0], current_calories)
        max_calories.sort()
        current_calories = 0

max_calories[0] = max(max_calories[0], current_calories)
print(sum(max_calories))
