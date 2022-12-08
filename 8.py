def line_to_check(i, j, d):
    if d == "left":
        return lines[i][:j][::-1]
    if d == "right":
        return lines[i][j+1:]
    if d == "up":
        return ''.join([lines[k][j] for k in range(i)][::-1])
    if d == "down":
        return ''.join([lines[k][j] for k in range(i+1,len(lines))])

def is_visible_dir(i, j, d):
    l = line_to_check(i, j, d)
    if len(l) == 0:
        return True
    return int(lines[i][j]) > max(list(map(int,list(l))))

def is_visible(i, j):
    for d in ("left", "right", "up", "down"):
        if is_visible_dir(i, j, d):
            return True
    return False

def get_nearest_dir(i, j, d):
    l = line_to_check(i, j, d)
    for c in range(len(l)):
        if l[c] >= lines[i][j]:
            return c+1
    return len(l)

def get_scenic(i, j):
    p = 1
    for d in ("left", "right", "up", "down"):
        p *= get_nearest_dir(i, j, d)
    return p

lines = open("8.dat").read().splitlines()

s=0
t=0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        s += is_visible(i,j)
        t = max(t, get_scenic(i,j))
print(s,t)
