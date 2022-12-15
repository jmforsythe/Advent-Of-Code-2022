import re

# Triangle ineq:
# d(a,b) + d(b,c) >= d(a,c)

def dist(a, b):
    dx = abs(a[0]-b[0])
    dy = abs(a[1]-b[1])
    return dx+dy

def simplify_overlap(l):
    ptr = 0
    while ptr+1 < len(l):
        left = l[ptr]
        right = l[ptr+1]
        if left[1] >= right[0]-1:
            combined = left[0], max(left[1], right[1])
            l.remove(left)
            l.remove(right)
            l.insert(ptr, combined)
        else:
            ptr += 1

def blocked_area_at_Y(sensors, beacons, Y):
    distances = [dist(sensors[i], beacons[i]) for i in range(len(sensors))]
    areas = []
    for i in range(len(sensors)):
        leftover = distances[i] - abs(Y-sensors[i][1])
        if leftover >= 0:
            areas.append((sensors[i][0]-leftover, sensors[i][0] + leftover))

    areas.sort()

    simplify_overlap(areas)

    return areas

def blocked_area_at_X(sensors, beacons, X):
    distances = [dist(sensors[i], beacons[i]) for i in range(len(sensors))]
    areas = []
    for i in range(len(sensors)):
        leftover = distances[i] - abs(X-sensors[i][0])
        if leftover >= 0:
            areas.append((sensors[i][1]-leftover, sensors[i][1] + leftover))

    areas.sort()

    simplify_overlap(areas)

    return areas

def in_areas(x, areas):
    for area in areas:
        if area[0] <= x and x <= area[1]:
            return True
    return False


def main():
    lines = open("15.dat").read().splitlines()

    sensors = []
    beacons = []

    Y = 2000000

    regex = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")
    for line in lines:
        r = regex.match(line)
        x1, y1, x2, y2 = tuple(map(int, r.groups()))
        sensors.append((x1,y1))
        beacons.append((x2,y2))
    
    s = tuple(sensors)
    b = tuple(beacons)

    areas = blocked_area_at_Y(s, b, Y)

    print(sum([1+a[1]-a[0] for a in areas]) - len(set([beacon for beacon in beacons if beacon[1] == Y])))

    only_spot = None

    for x in range(4000000, -1, -1):
        if x%(4000000//100) == 0:
            print(f"{100 - x//(4000000//100)}% searched")
        areas = blocked_area_at_X(s, b, x)
        if len(areas) == 1 and areas[0][0] <= 0 and areas[0][1] >= 4000000:
            continue
        else:
            assert(areas[0][1] + 2 == areas[1][0], "Something has gone wrong")
            only_spot = (x, areas[0][1]+1)
            break
    
    if only_spot:
        print(4000000 * only_spot[0] + only_spot[1])

if __name__ == "__main__":
    main()
