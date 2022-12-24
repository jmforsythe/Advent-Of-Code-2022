import functools

dir_to_sym = {
    1+0j : ">",
    0+1j : "^",
    -1+0j : "<",
    0-1j : "v"
}
sym_to_dir = {dir_to_sym[key] : key for key in dir_to_sym}

def read_input():
    lines = open("24.dat").read().splitlines()
    blizzards, walls = set(), set()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            pos = complex(j,-i)
            c = lines[i][j]
            if c == "#": walls.add(pos)
            elif c == ".": continue
            else: blizzards.add((pos, sym_to_dir[c]))
    return frozenset(blizzards), frozenset(walls)

@functools.cache
def next_pos(b, walls):
    if b[0]+b[1] not in walls:
        return (b[0]+b[1],b[1])
    else:
        i = 1
        while b[0] - i*b[1] not in walls:
            i += 1
        return (b[0]-(i-1)*b[1], b[1])

@functools.cache
def move_blizzards(blizzards, walls):
    blizzards_next = set()
    for b in blizzards:
        blizzards_next.add(next_pos(b, walls))
    return frozenset(blizzards_next)

def print_board(blizzards, walls):
    top = int(max(w.imag for w in walls))
    bottom = int(min(w.imag for w in walls))
    right = int(max(w.real for w in walls))
    left = int(min(w.real for w in walls))
    blizzards_no_dir = {b[0] for b in blizzards}
    for i in range(top, bottom-1, -1):
        line = []
        for j in range(left, right+1):
            x = complex(j,i)
            if x in walls: line.append("#")
            elif x in blizzards_no_dir:
                y = [dir_to_sym[d] for d in dir_to_sym if (x,d) in blizzards]
                if len(y) == 1:
                    line.append(y[0])
                else:
                    line.append(str(len(y)))
            else: line.append(".")
        print("".join(line))

@functools.cache
def get_valid_moves(pos, blizzards, walls):
    return (pos+i for i in (0+0j, 1+0j, 0+1j, -1+0j, 0-1j) if pos+i not in blizzards | walls
            and min(k.real for k in walls)<=(pos+i).real<=max(k.real for k in walls)
            and min(k.imag for k in walls)<=(pos+i).imag<=max(k.imag for k in walls))

@functools.cache
def get_next_possible(cur_possible, blizzards, walls):
    return (i for pos in cur_possible for i in get_valid_moves(pos, blizzards, walls))

def main():
    blizzards, walls = read_input()
    possible_pos = frozenset(complex(i,0) for i in range(int(max(x.real for x in walls))) if complex(i,0) not in walls)
    end_pos = tuple(complex(i,min(x.imag for x in walls)) for i in range(int(max(x.real for x in walls))) if complex(i,min(x.imag for x in walls)) not in walls)[0]

    i = 0
    while end_pos not in possible_pos:
        blizzards = move_blizzards(blizzards, walls)
        possible_pos = frozenset(get_next_possible(possible_pos, frozenset(b[0] for b in blizzards), walls))
        i += 1
    print(i)

    possible_pos = frozenset((end_pos,))
    end_pos = [complex(i,0) for i in range(int(max(x.real for x in walls))) if complex(i,0) not in walls][0]
    while end_pos not in possible_pos:
        blizzards = move_blizzards(blizzards, walls)
        possible_pos = frozenset(get_next_possible(possible_pos, frozenset(b[0] for b in blizzards), walls))
        i += 1

    possible_pos = frozenset((end_pos,))
    end_pos = [complex(i,min(x.imag for x in walls)) for i in range(int(max(x.real for x in walls))) if complex(i,min(x.imag for x in walls)) not in walls][0]
    while end_pos not in possible_pos:
        blizzards = move_blizzards(blizzards, walls)
        possible_pos = frozenset(get_next_possible(possible_pos, frozenset(b[0] for b in blizzards), walls))
        i += 1
    print(i)

if __name__ == "__main__":
    main()