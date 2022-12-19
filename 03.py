def get_in_common(a, b):
    d = {}
    out = {}
    for i in a:
        d[i] = 1
    for j in b:
        if j in d:
            out[j] = 1
    return ''.join(out.keys())

def priority(c):
    x = ord(c)
    if x >= ord('a'):
        return x - ord('a') + 1
    return x - ord('A') + 27

def line_priority(l):
    s = 0
    line = l.rstrip()
    n = len(line)
    first = line[:n//2]
    second = line[n//2:]
    c = get_in_common(first, second)
    for i in c:
        s += priority(i)
    return s

s=0
s2 = 0
group_of_3 = []
with open("3.dat") as f:
    for l in f:
        s += line_priority(l)
        group_of_3.append(l.rstrip())
        if len(group_of_3) == 3:
            a, b, c = group_of_3
            badge = get_in_common(a, get_in_common(b, c))
            group_of_3 = []
            s2 += priority(badge)
print(s, s2)
