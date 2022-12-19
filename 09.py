def print_board(k):
    pos = []
    ptr = head
    while ptr != None:
        pos.append((ptr.x,ptr.y))
        ptr = ptr.child
    print(pos)
    for i in range(-5, 5):
        line = ""
        for j in range(-5,5):
            if (j,-i) in pos:
                line += str(pos.index((j,-i)))
            else:
                line += "."
        print(line)

def is_touching(a,b):
    dx = abs(a.x-b.x)
    dy = abs(a.y-b.y)
    if dx <= 1 and dy <=1:
        return True
    return False

seen = {(0,0)}

class Knot:
    def __init__(self, parent, num, x=0, y=0):
        self.parent = parent
        self.child = None
        self.num = num
        self.x = x
        self.y = y
    def add_child(self, k):
        self.child = k
        return self.child
    def print_knot(self):
        print(self.num, self.x, self.y)
        if self.child:
            self.child.print_knot()
    def move(self, x, y):
        oldx = self.x
        oldy = self.y
        self.x = x
        self.y = y
        if self.child != None and not is_touching(self, self.child):
            dx = self.x - self.child.x
            adx = max(1,abs(dx))
            dy = self.y - self.child.y
            ady = max(1,abs(dy))
            self.child.move(self.child.x + dx/adx, self.child.y + dy/ady)
        elif self.child == None:
            seen.add((self.x, self.y))

head = Knot(None, 0)
head.add_child(Knot(head, 12))
ptr = head
for i in range(1,10):
    ptr = ptr.add_child(Knot(ptr, i))

with open("9.dat") as f:
    for line in f:
        a, b = line.rstrip().split()
        for _ in range(int(b)):
            if a == "U":
                head.move(head.x, head.y+1)
            elif a == "D":
                head.move(head.x, head.y-1)
            elif a == "L":
                head.move(head.x-1, head.y)
            elif a == "R":
                head.move(head.x+1, head.y)
print(len(seen))
