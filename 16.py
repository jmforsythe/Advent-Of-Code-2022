import re
import functools

ids = {}
id_ctr = 0
def id(name):
    global id_ctr
    if name not in ids:
        ids[name] = id_ctr
        id_ctr += 1
    return ids[name]

def main():
    regex = re.compile(r"Valve (.*) has.*=(\d+);.*ves? (.*)")
    lines = open("16.dat").read().splitlines()
    flows = [0 for i in range(len(lines))]
    adjacency_matrix = [[0 for i in range(len(lines))] for j in range(len(lines))]
    for line in lines:
        m = regex.match(line)
        valve = m.group(1)
        flow = m.group(2)
        out = m.group(3).split(", ")
        id(valve)
        flows[id(valve)] = int(flow)
        for v in out:
            adjacency_matrix[id(v)][id(valve)] = 1
    NUM = len(lines)
    
    def dist_pop(i,j):
        if i==j:
            return 0
        if adjacency_matrix[i][j]:
            return adjacency_matrix[i][j]
        return 9999999
    dist = [[dist_pop(i,j) for j in range(NUM)] for i in range(NUM)]
    for a in range(NUM):
        for b in range(NUM):
            for c in range(NUM):
                dist[b][c] = min(dist[b][c], dist[b][a] + dist[a][c])
    
    @functools.cache
    def get_best(curPos, disabled, time_left, with_elephant):
        if time_left <= 0:
            return 0
        best = 0
        for dest in disabled:
            best = max(best, flows[dest]*(time_left - dist[curPos][dest] - 1) +
                             get_best(dest, disabled-{dest}, time_left - dist[curPos][dest] - 1, with_elephant))
        if with_elephant:
            best = max(best, get_best(id("AA"), disabled, 26, False))
        return best

    print(get_best(id("AA"), frozenset(i for i in range(NUM) if flows[i]>0), 30, False))
    print(get_best(id("AA"), frozenset(i for i in range(NUM) if flows[i]>0), 26, True))

if __name__ == "__main__":
    main()