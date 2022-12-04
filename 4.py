def to_int(a,b,c,d):
    return int(a), int(b), int(c), int(d)

count = 0
count2 = 0
with open("4.dat") as f:
    for l in f:
        line = l.rstrip()
        a, b = line.split(",")
        a1, a2 = a.split("-")
        b1, b2 = b.split("-")
        a1,a2,b1,b2 = to_int(a1,a2,b1,b2)
        if (a1 <= b1 and b2 <= a2) or (b1 <= a1) and (a2 <= b2):
            count += 1
        if (a1 <= b1 and b1 <= a2) or (b1 <= a1 and a1 <= b2):
            count2 += 1

print(count, count2)