WIDTH = 7

class Rock:
    def __init__(self, type):
        if type == "hor":
            self.shape = [["#","#","#","#"]]
            self.to_check = [(0,-1),(1,-1),(2,-1),(3,-1)]
            self.check_left = [(-1,0)]
            self.check_right = [(4,0)]
        elif type == "plus":
            self.shape = [[".","#","."],
                          ["#","#","#"],
                          [".","#","."]
                         ]
            self.to_check = [(0,0),(1,-1),(2,0)]
            self.check_left = [(0,2),(-1,1),(0,0)]
            self.check_right = [(2,2),(3,1),(2,0)]
        elif type == "corner":
            self.shape = [[".",".","#"],
                          [".",".","#"],
                          ["#","#","#"]
                         ]
            self.to_check = [(0,-1),(1,-1),(2,-1)]
            self.check_left = [(-1,0),(1,1),(1,2)]
            self.check_right = [(3,i) for i in range(3)]
        elif type == "ver":
            self.shape = [["#"],["#"],["#"],["#"]]
            self .to_check = [(0,-1)]
            self.check_left = [(-1,i) for i in range(4)]
            self.check_right = [(1,i) for i in range(4)]
        elif type == "square":
            self.shape = [["#","#"],
                          ["#","#"]
                         ]
            self.to_check = [(0,-1),(1,-1)]
            self.check_left = [(-1,i) for i in range(2)]
            self.check_right = [(2,i) for i in range(2)]

def get_starting_pos(board):
    highest_rock = 0
    for i in range(len(board)-1, -1, -1):
        if "#" in board[i] or "-" in board[i]:
            highest_rock = i
            break
    return (2,highest_rock+4)

def print_chamber(board):
    for line in board[::-1]:
        print(''.join(line))

def check_down(board, rock, cur_pos):
    for i in rock.to_check:
        if board[cur_pos[1]+i[1]][cur_pos[0]+i[0]] != ".":
            return False
    return True

def check_left(board, rock, cur_pos):
    for i in rock.check_left:
        if cur_pos[0]+i[0] < 0:
            return False
        if board[cur_pos[1]+i[1]][cur_pos[0]+i[0]] != ".":
            return False
    return True

def check_right(board, rock, cur_pos):
    for i in rock.check_right:
        if cur_pos[0]+i[0] >= WIDTH:
            return False
        if board[cur_pos[1]+i[1]][cur_pos[0]+i[0]] != ".":
            return False
    return True

def write_rock(board, rock, cur_pos):
    x = len(rock.shape[0])
    y = len(rock.shape)
    for i in range(y):
        for j in range(x):
            if rock.shape[i][j] == "#":
                board[cur_pos[1]+y-i-1][cur_pos[0]+j] = "#"

def main():
    moves = open("17.dat").read().rstrip()
    #moves = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

    move_index = -1
    n = len(moves)
    def next_move():
        nonlocal move_index, n
        move_index += 1
        return moves[move_index%n]

    rock_index = -1
    def get_next_rock():
        nonlocal rock_index
        rock_index += 1
        return Rock(["hor", "plus", "corner", "ver", "square"][rock_index%5])

    chamber = [["-" for i in range(WIDTH)]] + [["." for i in range(WIDTH)] for i in range(9)]
    cur_pos = get_starting_pos(chamber)
    cur_rock = get_next_rock()
    cur_pos = (cur_pos[0], cur_pos[1] + 1)

    num_moves = 0
    num_rocks = 0
    while num_rocks < 2022:
        num_moves += 1
        move = next_move()

        # Do rock up/down
        if check_down(chamber, cur_rock, cur_pos):
            cur_pos = (cur_pos[0], cur_pos[1]-1)
        else:
            write_rock(chamber, cur_rock, cur_pos)
            cur_rock = get_next_rock()
            cur_pos = get_starting_pos(chamber)
            rows_to_add = max(0, (cur_pos[1] + len(cur_rock.shape)) - len(chamber))
            chamber += [["." for i in range(WIDTH)] for j in range(rows_to_add)]
            num_rocks += 1
        # Do sideways
        if move == "<" and check_left(chamber, cur_rock, cur_pos):
            cur_pos = (cur_pos[0]-1, cur_pos[1])
        if move == ">" and check_right(chamber, cur_rock, cur_pos):
            cur_pos = (cur_pos[0]+1, cur_pos[1])
    print(get_starting_pos(chamber)[1]-4)

def main2():
    moves = open("17.dat").read().rstrip()
    #moves = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

    move_index = -1
    n = len(moves)
    def next_move():
        nonlocal move_index, n
        move_index += 1
        return moves[move_index%n]

    rock_index = -1
    def get_next_rock():
        nonlocal rock_index
        rock_index += 1
        return Rock(["hor", "plus", "corner", "ver", "square"][rock_index%5])

    chamber = [["-" for i in range(WIDTH)]] + [["." for i in range(WIDTH)] for i in range(9)]
    cur_pos = get_starting_pos(chamber)
    cur_rock = get_next_rock()
    cur_pos = (cur_pos[0], cur_pos[1] + 1)

    num_moves = 0
    num_rocks = 0

    finding_cycle = True
    found_cycle = False

    while True:
        if num_moves > 0 and num_moves % n == 0:
            if finding_cycle:
                r_index = rock_index % 5
                finding_cycle = False
                cycle_start_rocks = num_rocks
                cycle_start_height = get_starting_pos(chamber)[1]-4
            elif rock_index % 5 == r_index:
                cycle_end_rocks = num_rocks
                cycle_end_height = get_starting_pos(chamber)[1]-4
                rocks_delta = cycle_end_rocks - cycle_start_rocks
                height_delta = cycle_end_height - cycle_start_height
                rocks_after_precycle = 1000000000000 - cycle_start_rocks
                num_cycles = rocks_after_precycle // rocks_delta
                rocks_remaining = rocks_after_precycle - num_cycles*rocks_delta
                found_cycle = True
        if found_cycle and num_rocks == cycle_end_rocks+rocks_remaining:
            height_bonus = get_starting_pos(chamber)[1]-4 - cycle_end_height
            print(height_delta*num_cycles+cycle_start_height+height_bonus)
            break


        move = next_move()

        # Do rock up/down
        if check_down(chamber, cur_rock, cur_pos):
            cur_pos = (cur_pos[0], cur_pos[1]-1)
        else:
            write_rock(chamber, cur_rock, cur_pos)
            cur_rock = get_next_rock()
            cur_pos = get_starting_pos(chamber)
            rows_to_add = max(0, (cur_pos[1] + len(cur_rock.shape)) - len(chamber))
            chamber += [["." for i in range(WIDTH)] for j in range(rows_to_add)]
            num_rocks += 1
        # Do sideways
        if move == "<" and check_left(chamber, cur_rock, cur_pos):
            cur_pos = (cur_pos[0]-1, cur_pos[1])
        if move == ">" and check_right(chamber, cur_rock, cur_pos):
            cur_pos = (cur_pos[0]+1, cur_pos[1])
        
        num_moves += 1

if __name__ == "__main__":
    main()
    main2()