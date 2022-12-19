import re
import copy

def convert_to_stacks(x):
    width = int((x[-1].rstrip().split(" ")[-1]))
    stacks = [[] for i in range(width)]
    for line in x[::-1][1:]:
        for i in range(width):
            c = 1 + (4*i)
            if line[c] != " ":
                stacks[i].append(line[c])
    return stacks

def move(stacks, source, dest):
    x = stacks[source-1].pop()
    stacks[dest-1].append(x)

def move2(stacks, source, dest, num):
    x = stacks[source-1][-num:]
    stacks[dest-1] += x
    stacks[source-1] = stacks[source-1][:-num]


top_dat = []

with open("5.dat") as f:
    for l in f:
        line = l.rstrip()
        if line == "":
            break
        else:
            top_dat.append(l)
    stacks = convert_to_stacks(top_dat)
    stacks2 = copy.deepcopy(stacks)

    match_string = r"move (\d+) from (\d+) to (\d+)"

    for l in f:
        x = re.match(match_string, l)
        num = int(x.group(1))
        source = int(x.group(2))
        dest = int(x.group(3))
        for i in range(num):
            move(stacks, source, dest)
        move2(stacks2, source, dest, num)
    
    out = ""
    for stack in stacks:
        out += stack[-1]
    print(out)

    out2 = ""
    for stack in stacks2:
        out2 += stack[-1]
    print(out2)
