def block_squares(board, point1, point2):
    dx = point1[0]-point2[0]
    dy = point1[1]-point2[1]
    assert(dx == 0 or dy == 0)
    if dx:
        for x in range(min(point1[0],point2[0]), max(point1[0],point2[0])+1):
            board[(x, point1[1])] = "#"
    elif dy:
        for y in range(min(point1[1],point2[1]), max(point1[1],point2[1])+1):
            board[(point1[0], y)] = "#"

def board_to_grid(board):
    # Must include (500, 0)
    xMin = min(500, min(key[0] for key in board))
    xMax = max(500, max(key[0] for key in board))
    yMin = min(0, min(key[1] for key in board))
    yMax = max(0, max(key[1] for key in board))

    grid = [["." for column in range(int(xMin), int(xMax)+1)] for row in range(int(yMin), int(yMax)+1)]
    yOffset = yMin
    xOffset = xMin
    for key in board:
        grid[key[1]-yOffset][key[0]-xOffset] = board[key]
    return grid

def print_board(board):
    grid = board_to_grid(board)
    for line in grid:
        print(''.join(line))

def drop_grain(board):
    cur_pos = [500,0]
    yMax = max(key[1] for key in board)
    while cur_pos[1] < yMax:
        if (cur_pos[0], cur_pos[1]+1) not in board:
            cur_pos[1] += 1
        elif (cur_pos[0]-1, cur_pos[1]+1) not in board:
            cur_pos[0] += -1
            cur_pos[1] += 1
        elif (cur_pos[0]+1, cur_pos[1]+1) not in board:
            cur_pos[0] += 1
            cur_pos[1] += 1
        else:
            board[(cur_pos[0], cur_pos[1])] = "o"
            return True
    return False

def drop_grain2(board, yMax):
    cur_pos = [500,0]
    while cur_pos[1] < yMax + 4:
        if cur_pos[1] >= yMax + 1:
            board[(cur_pos[0], cur_pos[1])] = "o"
            return True
        elif (cur_pos[0], cur_pos[1]+1) not in board:
            cur_pos[1] += 1
        elif (cur_pos[0]-1, cur_pos[1]+1) not in board:
            cur_pos[0] += -1
            cur_pos[1] += 1
        elif (cur_pos[0]+1, cur_pos[1]+1) not in board:
            cur_pos[0] += 1
            cur_pos[1] += 1
        else:
            board[(cur_pos[0], cur_pos[1])] = "o"
            if cur_pos[0] == 500 and cur_pos[1] == 0:
                return False
            return True
    

def main():
    board = {}

    lines = open("14.dat").read().splitlines()
    paths = [line.split(" -> ") for line in lines]
    for path in paths:
        c = [list(map(int, coords.split(","))) for coords in path]
        # Just in case only one point
        board[(c[0][0], c[0][1])] = "#"
        for i in range(1, len(c)):
            block_squares(board, c[i-1], c[i])
    
    count = 0
    while drop_grain(board):
        count += 1

    print_board(board)
    print()
    print(count)

    yMax = max(key[1] for key in board)
    while drop_grain2(board, yMax): 
        pass
    print_board(board)
    print(list(board.values()).count("o"))


if __name__ == "__main__":
    main()
