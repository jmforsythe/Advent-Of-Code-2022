import re
import functools

def main():
    text_dict = {}
    for line in open("21.dat").read().splitlines():
        monkey, val = line.split(": ")
        text_dict[monkey] = val

    q = ["root"]

    for i in q:
        val = text_dict[i]
        if m := re.match(r"(.*) [\+\-\*\/] (.*)", val):
            q.extend(m.groups())

    vals = {}

    for i in q[::-1]:
        if i not in vals:
            text = text_dict[i]
            try:
                vals[i] = int(text)
            except:
                if m := re.match(r"(.*) \+ (.*)", text):
                    vals[i] = int(vals[m.group(1)]) + int(vals[m.group(2)])
                elif m := re.match(r"(.*) \- (.*)", text):
                    vals[i] = int(vals[m.group(1)]) - int(vals[m.group(2)])
                elif m := re.match(r"(.*) \* (.*)", text):
                    vals[i] = int(vals[m.group(1)]) * int(vals[m.group(2)])
                elif m := re.match(r"(.*) \/ (.*)", text):
                    vals[i] = int(vals[m.group(1)]) / int(vals[m.group(2)])

    print(vals["root"])

def search(func, max_pow):
    centre = 0
    for pow in range(max_pow,0,-1):
        for i in range(centre-10**pow, centre+10**pow, 10**(pow-1)):
            if func(i) == 0:
                return i
            if (func(i) > 0 and func(i+10**(pow-1)) < 0) or (func(i) < 0 and func(i+10**(pow-1)) > 0):
                centre = i
                break

def main2():
    text_dict = {}
    for line in open("21.dat").read().splitlines():
        monkey, val = line.split(": ")
        text_dict[monkey] = val

    q = ["root"]

    for i in q:
        val = text_dict[i]
        if m := re.match(r"(.*) [\+\-\*\/] (.*)", val):
            q.extend(m.groups())
    
    @functools.cache
    def func(humn_val):
        vals = {}
        vals["humn"] = humn_val
        for i in q[::-1]:
            if i not in vals:
                text = text_dict[i]
                try:
                    vals[i] = int(text)
                except:
                    if m := re.match(r"(.*) \+ (.*)", text):
                        vals[i] = int(vals[m.group(1)]) + int(vals[m.group(2)])
                    elif m := re.match(r"(.*) \- (.*)", text):
                        vals[i] = int(vals[m.group(1)]) - int(vals[m.group(2)])
                    elif m := re.match(r"(.*) \* (.*)", text):
                        vals[i] = int(vals[m.group(1)]) * int(vals[m.group(2)])
                    elif m := re.match(r"(.*) \/ (.*)", text):
                        vals[i] = int(vals[m.group(1)]) / int(vals[m.group(2)])
        p1 = vals[q[1]]
        p2 = vals[q[2]]
        return p1-p2

    answer = None
    max_pow = 10
    while answer == None:
        max_pow += 1
        answer = search(func, max_pow)
    print(answer)

if __name__ == "__main__":
    main()
    main2()
