

class Register:
    def __init__(self):
        self.value = 1
        self.cycle = 0
        self.signal_strength = self.cycle * self.value
        self.history = {self.cycle: (self.value, self.signal_strength)}

    def increment(self):
        self.cycle += 1
        self.signal_strength = self.cycle * self.value
        self.history[self.cycle] = (self.value, self.signal_strength)

    def instruct(self, cmd):
        cmd_split = cmd.split(' ')
        if cmd_split[0] == 'noop':
            self.increment()
        elif cmd_split[0] == 'addx':
            self.increment()
            self.increment()
            self.value += int(cmd_split[1])


input_file = open('input/input_day10_1.txt', 'r').read().strip().split('\n')
X = Register()

for line in input_file:
    X.instruct(line)
    if X.cycle > 220:
        print(sum([X.history[cycle][1] for cycle in [20 + 40*i for i in range(6)]]))
        break
