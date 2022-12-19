cur = 0
cur_max = 0
cur_second = 0
cur_third = 0

def adjust_top(c, f, s, t):
    o = sorted([c,f,s,t])[::-1]
    return o[:-1]

    

with open("1.dat") as f:
    for l in f:
        line = l.rstrip()
        if line == "":
            cur_max, cur_second, cur_third = adjust_top(cur, cur_max, cur_second, cur_third)
            cur = 0
        else:
            cur += int(line)
cur_max, cur_second, cur_third = adjust_top(cur, cur_max, cur_second, cur_third)
print(cur_max, cur_second, cur_third)
print(cur_max + cur_second + cur_third)
