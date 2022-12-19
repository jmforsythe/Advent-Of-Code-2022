def get_sides(x,y,z):
    return {(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}

def main():
    cubes = set()
    lines = open("18.dat").read().splitlines()
    for line in lines:
        x,y,z = (int(_) for _ in line.split(","))
        cubes.add((x,y,z))
    sa = 0
    for cube in cubes:
        for side in get_sides(cube[0], cube[1], cube[2]):
            if side not in cubes:
                sa += 1
    print(sa)

    # Part 2
    xmin = min(map(lambda x: x[0], cubes))
    xmax = max(map(lambda x: x[0], cubes))
    ymin = min(map(lambda x: x[1], cubes))
    ymax = max(map(lambda x: x[1], cubes))
    zmin = min(map(lambda x: x[2], cubes))
    zmax = max(map(lambda x: x[2], cubes))

    queue = [(xmin,ymin,zmin)]
    visible = set()
    while len(queue)>0:
        cur = queue.pop()
        for side in get_sides(cur[0],cur[1],cur[2]):
            if side not in cubes and side not in visible:
                if (xmin-1<=side[0]<=xmax+1 and ymin-1<=side[1]<=ymax+1 and zmin-1<=side[2]<=zmax+1):
                    queue.append(side)
        visible.add(cur)

    sa = 0
    for cube in cubes:
        for side in get_sides(cube[0], cube[1], cube[2]):
            if side in visible:
                sa += 1
    print(sa)

if __name__ == "__main__":
    main()
