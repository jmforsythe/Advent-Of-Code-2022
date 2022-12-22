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
        return (i+direction[0], j+direction[1])
    else:
        step = 0
        while is_valid_pos(board, i-step*direction[0], j-step*direction[1]):
            step += 1
        return (i-(step-1)*direction[0], j-(step-1)*direction[1])

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
            x = get_dest(board, *cur_pos, direction)
            if board[x[0]][x[1]] == ".":
                cur_pos = x
        if ins[1] == "L":
            direction = anticlockwise[direction]
        elif ins[1] == "R":
            direction = clockwise[direction]
    out = (cur_pos[0]+1, cur_pos[1]+1, list(clockwise.keys()).index(direction))
    print(1000*out[0] + 4*out[1] + out[2])

if __name__ == "__main__":
    main(get_dest_1)