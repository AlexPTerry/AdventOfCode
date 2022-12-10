

class CRT:
    def __init__(self):
        self.display = [[' ' for _ in range(40)] for __ in range(6)]
        self.write_pos = [0, 0]

    def move_write(self):
        self.write_pos[0] = self.write_pos[0] + (self.write_pos[1] + 1) // 40
        self.write_pos[1] = (self.write_pos[1] + 1) % 40

    def write(self, value):
        if abs(self.write_pos[1] - value) <= 1:
            self.display[self.write_pos[0]][self.write_pos[1]] = '#'
        else:
            self.display[self.write_pos[0]][self.write_pos[1]] = '.'


class Register:
    def __init__(self):
        self.value = 1
        self.cycle = 0
        self.signal_strength = self.cycle * self.value
        self.history = {self.cycle: (self.value, self.signal_strength)}
        self.crt = CRT()

    def increment(self):
        self.cycle += 1
        self.crt.move_write()
        self.signal_strength = self.cycle * self.value
        self.history[self.cycle] = (self.value, self.signal_strength)

    def instruct(self, cmd):
        cmd_split = cmd.split(' ')
        if cmd_split[0] == 'noop':
            self.crt.write(self.value)
            self.increment()
        elif cmd_split[0] == 'addx':
            self.crt.write(self.value)
            self.increment()
            self.crt.write(self.value)
            self.increment()
            self.value += int(cmd_split[1])


input_file = open('input/input_day10_1.txt', 'r').read().strip().split('\n')
X = Register()

for line in input_file:
    X.instruct(line)
    if X.cycle > 239:
        break

for i in range(6):
    print(''.join(X.crt.display[i]))

