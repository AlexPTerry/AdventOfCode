
input_file = open('input/input_day25_1.txt', 'r').read().strip().split('\n')

conversions = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
reverse = {val: key for key, val in conversions.items()}

number = 0
for line in input_file:
    for i, char in enumerate(line):
        power = len(line)-i-1
        number += 5**power*conversions[char]


snafu = ''

while number > 0:
    remainder = number % 5
    number = number // 5
    if remainder in {3, 4}:
        remainder -= 5
        number += 1
    snafu = reverse[remainder] + snafu
    print(number, remainder)

print(snafu)



