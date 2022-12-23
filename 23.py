def add(a,b):
    return (a[0]+b[0], a[1]+b[1])

N = (-1,0)
E = (0,1)
S = (1,0)
W = (0,-1)
NE = add(N,E)
SE = add(S,E)
SW = add(S,W)
NW = add(N,W)

def get_moves(round_num):
    out = []
    out.append((lambda pos: (add(pos,N), add(pos,NE), add(pos,NW)), lambda x: add(x,N),"NORTH"))
    out.append((lambda pos: (add(pos,S), add(pos,SE), add(pos,SW)), lambda x: add(x,S),"SOUTH"))
    out.append((lambda pos: (add(pos,W), add(pos,NW), add(pos,SW)), lambda x: add(x,W),"WEST"))
    out.append((lambda pos: (add(pos,E), add(pos,NE), add(pos,SE)), lambda x: add(x,E),"EAST"))
    return out[round_num%4:] + out[:round_num%4]

def first_half(elves, round_num):
    moves = get_moves(round_num)
    elves_map = dict()
    for elf in elves:
        elves_map[elf] = elf
        if any(add(elf,x) in elves for x in (N,E,S,W,NE,SE,SW,NW)):
            for to_check, move, name in get_moves(round_num):
                if all((p not in elves for p in to_check(elf))):
                    elves_map[elf] = move(elf)
                    break
    return elves_map

def second_half(elves_map):
    keys_of_duplicates = [elf for elf in elves_map if list(elves_map.values()).count(elves_map[elf]) > 1]
    for key in keys_of_duplicates:
        elves_map[key] = key
    return set(elves_map.values())

def do_round(elves, round_num):
    elves_map = first_half(elves, round_num)
    return second_half(elves_map)

    assert(len(elves) == len(elves_next))
    return elves_next

def print_elves(elves):
    for i in range(min(elf[0] for elf in elves), max(elf[0] for elf in elves)+1):
        line = []
        for j in range(min(elf[1] for elf in elves), max(elf[1] for elf in elves)+1):
            if (i,j) in elves:
                line.append("#")
            else:
                line.append(".")
        print("".join(line))

def main():
    elves = set()
    lines = open("23.dat").read().splitlines()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                elves.add((i,j))

    no_move = None

    for round_num in range(10):
        new_elves = do_round(elves, round_num)
        if no_move == None and elves == new_elves:
            no_move = round_num+1
        elves = new_elves

    ymin = min(elf[0] for elf in elves)
    ymax = max(elf[0] for elf in elves)
    xmin = min(elf[1] for elf in elves)
    xmax = max(elf[1] for elf in elves)
    print(sum((i,j) not in elves for i in range(ymin, ymax+1) for j in range(xmin, xmax+1)))

    round_num = 10
    while no_move == None:
        new_elves = do_round(elves, round_num)
        if no_move == None and elves == new_elves:
            no_move = round_num+1
        elves = new_elves
        round_num += 1
    print(no_move)

if __name__ == "__main__":
    main()