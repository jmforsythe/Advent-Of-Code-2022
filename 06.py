with open("6.dat") as f:
    data = f.read()

def do_thing(data, num):
    i = 0
    s = []
    for c in data:
        if len(s) == num:
            break
        elif c in s:
            k = s.index(c)
            s = s[k+1:]
        s.append(c)
        i += 1
    return i

print(do_thing(data, 4))
print(do_thing(data, 14))