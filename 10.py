cycle = 0
reg = 1
sigs = []
pixels = ["." for i in range(240)]

with open("10.dat") as f:
    for line in f:
        a = line.rstrip().split()
        ins = a[0]
        if len(a) > 1:
            num = a[1]
        if ins == "addx":
            for _ in range(2):
                cycle += 1
                if (cycle%40) == 20:
                    signal_strength = cycle * reg
                    sigs.append(signal_strength)
                if abs(((cycle+39)%40)-reg) <= 1:
                    pixels[cycle-1] = "#"
            reg += int(num)
        elif ins == "noop":
            cycle += 1
            if (cycle%40) == 20:
                signal_strength = cycle * reg
                sigs.append(signal_strength)
            if abs(((cycle+39)%40)-reg) <= 1:
                pixels[cycle-1] = "#"
            
                

print(sum(sigs))
for i in range(6):
    print("".join(pixels[i*40:(i+1)*40]))
