DEBUG = 0
import math

class Vertex:
    def __init__(self, val):
        self.val = val
        self.neighbours = []
        self.visited = False
        self.prev = None
        self.tent_dist = math.inf
        self.in_queue = False
        global DEBUG
        self.debug = DEBUG
        DEBUG += 1
    def add_neighbour(self, v):
        self.neighbours.append(v)

def reset_node(node):
    node.visited = False
    node.tent_dist = math.inf
    node.in_queue = False

def val_to_comp(node):
    x = node.val
    if x == "E":
        return 26
    if x == "S":
        return 1
    return ord(x)-ord("a")+1

def build_graph(lines):
    nodes = []
    for line in lines:
        node_line = []
        for c in line:
            node_line.append(Vertex(c))
        nodes.append(node_line)
    n = len(nodes)
    for i in range(n):
        m = len(nodes[i])
        for j in range(m):
            cur = nodes[i][j]
            for (a,b) in ((0,1), (0,-1), (1,0), (-1,0)):
                if i+a >= 0 and i+a < n and j+b >= 0 and j+b < m:
                    comp = nodes[i+a][j+b]
                    x2 = val_to_comp(cur)
                    x1 = val_to_comp(comp)
                    if x1 + 1 >= x2:
                        cur.add_neighbour(comp)
    return nodes

def insert_into_queue(node, queue):
    n = len(queue)
    c = n
    node.in_queue = True
    x = val_to_comp(node)
    for i in range(len(queue)):
        if x < val_to_comp(queue[i]):
            c = i
    queue.insert(c, node)
    assert(n+1 == len(queue))

def update_pos(node, queue):
    queue.remove(node)
    node.in_queue = False
    insert_into_queue(node, queue)

def Dijkstra(start, end):
    queue = [start]
    start.tent_dist = 0
    i = 0
    while len(queue) > 0:
        i += 1
        if i%10000 == 0:
            print(i)
        if not queue[0].visited:
            queue[0].visited = True
            for n in queue[0].neighbours:
                if n.tent_dist > queue[0].tent_dist + 1:
                    n.tent_dist = queue[0].tent_dist + 1
                    if not n.visited:
                        if n.in_queue:
                            update_pos(n, queue)
                        else:
                            insert_into_queue(n, queue)
        queue[0].in_queue = False
        queue = queue[1:]
        if end.visited:
            return

def find_start(graph):
    for node in graph:
        if node.val == "S":
            return node
    return None

def find_end(graph):
    for node in graph:
        if node.val == "E":
            return node
    return None

def reset_graph(graph):
    for node in graph:
        reset_node(node)

def main():
    lines = open("12.dat").read().splitlines()
    # Flatten
    graph = [node for node_line in build_graph(lines) for node in node_line]
    start = find_start(graph)
    end = find_end(graph)
    Dijkstra(end, start)
    print(start.tent_dist)

    possible_lengths = [start.tent_dist]

    possible_starts = [n for n in graph if n.val == "a"]
    for n in possible_starts:
        if n.visited:
            possible_lengths.append(n.tent_dist)
    print(min(possible_lengths))

if __name__ == "__main__":
    main()
