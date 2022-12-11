import operator as op
from collections import deque


class Monkey:
    def __init__(self, starting_items, operation, test, result):
        self.items = deque(starting_items)
        self.operation = operation    # Format: new "op" old
        self.test = test
        self.result = result
        self.total_inspections = 0

    def inspect_item(self, item):
        binary = {'*': op.mul, '+': op.add, '-': op.sub, '/': op.truediv}
        self.total_inspections += 1
        if self.operation == 'old * old':
            return item ** 2
        return binary[self.operation.split(' ')[1]](item, int(self.operation.split(' ')[2]))

    def test_item(self, item):
        return item % self.test == 0

    def receive_item(self, item):
        self.items.append(item)

    def throw_item(self, monkey, item):
        self.items.popleft()
        monkey.receive_item(item)

    def inspect_all_items(self, monkey_list):
        for _ in range(len(self.items)):
            item = self.items[0]
            inspected_item = self.inspect_item(item) // 3
            if self.test_item(inspected_item):
                self.throw_item(monkey_list[self.result[0]], inspected_item)
            else:
                self.throw_item(monkey_list[self.result[1]], inspected_item)


input_file = open('input/input_day11_1.txt', 'r').read().strip()

monkey_list = []

for monkey_def in input_file.split('\n\n'):
    monkey_result = [-1, -1]
    for line in monkey_def.split('\n'):
        type = list(map(lambda x: x.strip(), line.split(':')))
        if type[0] == 'Starting items':
            monkey_starting_items = list(map(int, type[1].split(', ')))
        elif type[0] == 'Operation':
            monkey_operation = type[1].split('= ')[1]
        elif type[0] == 'Test':
            monkey_test = int(type[1].split('by ')[1])
        elif type[0] == 'If true':
            monkey_result[0] = int(type[1].split('monkey ')[1])
        elif type[0] == 'If false':
            monkey_result[1] = int(type[1].split('monkey ')[1])
    monkey_list.append(Monkey(monkey_starting_items, monkey_operation, monkey_test, monkey_result))

for _ in range(20):
    for i in range(len(monkey_list)):
        monkey_list[i].inspect_all_items(monkey_list)

inspections = [monkey.total_inspections for monkey in monkey_list]
sorted_inspections = sorted(inspections, reverse=True)
print(sorted_inspections[0] * sorted_inspections[1])

