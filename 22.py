import re

def is_valid_pos(board, i, j):
    if i<0 or i>=len(board):
        return False
    if j<0 or j>=len(board[i]):
        return False
    if board[i][j] == " ":
        return False
    return True

def get_dest_1(board, i, j, direction):
    if is_valid_pos(board, i+direction[0], j+direction[1]):
        return (i+direction[0], j+direction[1]), direction
    else:
        step = 0
        while is_valid_pos(board, i-step*direction[0], j-step*direction[1]):
            step += 1
        return (i-(step-1)*direction[0], j-(step-1)*direction[1]), direction

def get_dest_2(board, i, j, direction):
    if is_valid_pos(board, i+direction[0], j+direction[1]):
        return (i+direction[0], j+direction[1]), direction
    return edge_case(i, j, direction)

def edge_case(i, j, direction):
    i_region = i%50
    j_region = j%50
    if i == 0 and direction == (-1,0):
        if 50<=j<100:
            return (150+j_region, 0), clockwise[direction]
        elif 100<=j<150:
            return (199, j_region), direction
    if i == 49 and direction == (1,0):
        return (50+j_region, 99), clockwise[direction]
    if i == 100 and direction == (-1,0):
        return (50+j_region, 50), clockwise[direction]
    if i == 149 and direction == (1,0):
        return (150+j_region, 49), clockwise[direction]
    if i == 199 and direction == (1,0):
        return (0, 100+j_region), direction
    if j == 0 and direction == (0,-1):
        if 100<=i<150:
            return (49-i_region, 50), clockwise[clockwise[direction]]
        elif 150<=i<200:
            return (0, 50+i_region), anticlockwise[direction]
    if j == 50 and direction == (0,-1):
        if 0<=i<50:
            return (149-i_region, 0), clockwise[clockwise[direction]]
        elif 50<=i<100:
            return(100,0+i_region), anticlockwise[direction]
    if j == 49 and direction == (0,1):
        return (149, 50+i_region), anticlockwise[direction]
    if j == 99 and direction == (0,1):
        if 50<=i<100:
            return (49, 100+i_region), anticlockwise[direction]
        elif 100<=i<150:
            return (49-i_region, 149), clockwise[clockwise[direction]]
    if j == 149 and direction == (0,1):
        return (149-i_region, 99), clockwise[clockwise[direction]]

def get_start_pos(board):
    for i in range(len(board[0])):
        if board[0][i] == ".":
            return (0,i)

clockwise = {
    (0,1) : (1,0),
    (1,0) : (0,-1),
    (0,-1) : (-1,0),
    (-1,0) : (0,1)
}

anticlockwise = {
    (0,1) : (-1,0),
    (1,0) : (0,1),
    (0,-1) : (1,0),
    (-1,0) : (0,-1)
}

dir_symbol = {
    (0,1) : ">",
    (0,-1) : "<",
    (1,0) : "v",
    (-1,0) : "^"
}

def main(get_dest):
    lines = open("22.dat").read().splitlines()
    board = [[c for c in line] for line in lines[:-1]]
    instructions = []
    if lines[-1][0] in ("L","R"):
        instructions = [('0', lines[-1][0])]
    instructions.extend(re.findall(r"(\d+)([LR])", lines[-1]))
    if lines[-1][-1] not in ("L","R"):
        x = min(lines[-1][::-1].index("L"), lines[-1][::-1].index("L"))
        last_num = lines[-1][::-1][:x][::-1]
        instructions.append((last_num, None))

    direction = (0,1)
    cur_pos = get_start_pos(board)
    for ins in instructions:
        for i in range(int(ins[0])):
            x, d = get_dest(board, *cur_pos, direction)
            if board[x[0]][x[1]] != "#":
                board[cur_pos[0]][cur_pos[1]] = dir_symbol[direction]
                cur_pos = x
                direction = d
        out = (cur_pos[0]+1, cur_pos[1]+1, list(clockwise.keys()).index(direction))
        if ins[1] == "L":
            direction = anticlockwise[direction]
        elif ins[1] == "R":
            direction = clockwise[direction]
    out = (cur_pos[0]+1, cur_pos[1]+1, list(clockwise.keys()).index(direction))
    print(1000*out[0] + 4*out[1] + out[2])

def test_edge_case():
    for i in range(50):
        assert(edge_case(0,50+i,(-1,0)) == ((150+i,0), (0,1)))
        assert(edge_case(0,100+i,(-1,0)) == ((199,0+i),(-1,0)))
        assert(edge_case(49,100+i,(1,0)) == ((50+i,99),(0,-1)))
        assert(edge_case(100,0+i,(-1,0)) == ((50+i,50),(0,1)))
        assert(edge_case(149,50+i,(1,0)) == ((150+i,49),(0,-1)))
        assert(edge_case(199,0+i,(1,0)) == ((0,100+i),(1,0)))
        assert(edge_case(100+i,0,(0,-1)) == ((49-i,50), (0,1)))
        assert(edge_case(150+i,0,(0,-1)) == ((0,50+i),(1,0)))
        assert(edge_case(0+i,50,(0,-1)) == ((149-i,0),(0,1)))
        assert(edge_case(50+i,50,(0,-1)) == ((100,0+i),(1,0)))
        assert(edge_case(150+i,49,(0,1)) == ((149,50+i),(-1,0)))
        assert(edge_case(50+i,99,(0,1)) == ((49,100+i),(-1,0)))
        assert(edge_case(100+i,99,(0,1)) == ((49-i,149),(0,-1)))
        assert(edge_case(0+i,149,(0,1)) == ((149-i,99),(0,-1)))

if __name__ == "__main__":
    main(get_dest_1)
    test_edge_case()
    main(get_dest_2)
