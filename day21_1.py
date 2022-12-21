import operator as op

input_file = open('input/input_day21_1.txt', 'r').read().strip().split('\n')
monkey_dict = {}

for line in input_file:
    monkey_to_answer = line.split(': ')
    monkey_dict[monkey_to_answer[0]] = monkey_to_answer[1]


def search_monkeys(monkey):
    binary = {'*': op.mul, '+': op.add, '-': op.sub, '/': op.truediv}
    monkey_answer = monkey_dict[monkey].split()
    if len(monkey_answer) == 1:
        return int(monkey_answer[0])
    else:
        return int(binary[monkey_answer[1]](search_monkeys(monkey_answer[0]), search_monkeys(monkey_answer[2])))


print(search_monkeys('root'))




