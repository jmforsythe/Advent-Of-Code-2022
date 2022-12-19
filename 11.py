class Monkey:
    def __init__(self, items, operation, divis_by, true_num, false_num):
        self.items = items
        self.operation = operation
        self.divis_by = divis_by
        self.true_num = true_num
        self.false_num = false_num
        self.true_target = None
        self.false_target = None
        self.num_inspected = 0

    def set_target(self, t, f):
        self.true_target = t
        self.false_target = f

    def add_item(self, x):
        self.items.append(x)
    
    def inspect(self, num):
        self.num_inspected += 1
        num = self.operation(num)
        #num //= 3
        return num

    def do_turn(self):
        while len(self.items) > 0:
            to_send = self.items.pop(0)
            to_send = self.inspect(to_send)
            to_send = to_send % lcm
            if to_send % self.divis_by == 0:
                self.true_target.add_item(to_send)
            else:
                self.false_target.add_item(to_send)

def add(a,b):
    return a+b

def mult(a,b):
    return a*b

def make_op(operation):
    symbol, num = operation.split()
    if symbol == "+":
        func = add
    elif symbol == "*":
        func = mult
    
    if num == "old":
        def f(old):
            return func(old, old)
    else:
        def f(old):
            return func(old, int(num))
    return f


with open("11.dat") as f:
    l = f.read().splitlines()

monkeys = []
lcm = 1

for monkey in range((len(l)+1)//7):
    lines = l[monkey*7: (monkey+1)*7]
    starting_items = list(map(int, lines[1][18:].split(", ")))
    operation = lines[2][23:]
    divis_by = int(lines[3].split()[-1])
    monkey_throw_true = int(lines[4].split()[-1])
    monkey_throw_false = int(lines[5].split()[-1])
    monkeys.append(Monkey(starting_items, make_op(operation), divis_by, monkey_throw_true, monkey_throw_false))
    lcm *= divis_by

for monkey in monkeys:
    monkey.set_target(monkeys[monkey.true_num], monkeys[monkey.false_num])

for round in range(10000):
    for monkey in monkeys:
        monkey.do_turn()

ins = []

for monkey in monkeys:
    ins.append(monkey.num_inspected)
    print(monkey.num_inspected)

ins.sort()

print(ins[-1]*ins[-2])
