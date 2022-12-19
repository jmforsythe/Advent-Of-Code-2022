import functools

# -1 for less left<right, 0 for equal, 1 for left>right
def compare(left, right):
    if type(left) != type(right):
        if type(left) == type(1):
            return compare([left],right)
        else:
            return compare(left, [right])
    else:
        if type(left) == type(1):
            if left < right:
                return -1
            elif left == right:
                return 0
            elif left > right:
                return 1
        else:
            if len(left) == 0:
                if len(right) == 0:
                    return 0
                else:
                    return -1
            for i in range(len(left)):
                if i >= len(right):
                    return 1
                cmp = compare(left[i], right[i])
                if cmp != 0:
                    return cmp
            if len(left) < len(right):
                return -1
            return 0

def main():
    lines = open("13.dat").read().splitlines()
    packets = [eval(line) for line in lines if line != ""]
    pairs = [[packets[i], packets[i+1]] for i in range(0, len(packets), 2)]

    s = 0

    for i in range(len(pairs)):
        pair = pairs[i]
        cmp = compare(pair[0], pair[1])
        if cmp == -1:
            s += i+1

    print(s)

    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=functools.cmp_to_key(compare))
    print(packets.index([[2]])+1, packets.index([[6]])+1,
          (packets.index([[2]])+1) * (packets.index([[6]])+1))

if __name__ == "__main__":
    main()
