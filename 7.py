class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name
    def get_size(self, tracker):
        return self.size

class Directory:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.children = []
        self.size = 0
    def add_child_file(self, size, name):
        self.children.append(File(size, name))
    def add_child_dir(self, name):
        self.children.append(Directory(self, name))
    
    def get_size(self, tracker):
        self.size = sum([c.get_size(tracker) for c in self.children])
        if self.size <= 100000:
            tracker[0] += self.size
        if self.size >= tracker[2]-(70000000-30000000):
            if tracker[1] == None or self.size < tracker[1].size:
                tracker[1] = self
        return self.size

none_dir = Directory(None, None)
cur_dir = none_dir
none_dir.add_child_dir("/")

lines = open("7.dat").read().splitlines()
for line in lines:
    if line[0] == "$":
        if line[2:4] == "cd":
            dest = line.rstrip()[5:]
            if dest == "..":
                cur_dir = cur_dir.parent
            else:
                for d in cur_dir.children:
                    if d.name == dest:
                        cur_dir = d
    else:
        a, name = line.split()
        if a == "dir":
            cur_dir.add_child_dir(name)
        else:
            cur_dir.add_child_file(int(a), name)

tracker = [0, None, 999999999999]
tracker[2] = none_dir.get_size(tracker)
tracker[0] = 0
none_dir.get_size(tracker)
print(tracker[0], tracker[1].name, tracker[1].size)