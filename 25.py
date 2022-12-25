m = {
    "2" : 2,
    "1" : 1,
    "0" : 0,
    "-" : -1,
    "=" : -2
}

def from_SNAFU(num_string):
    i = 1
    out = 0
    for c in num_string[::-1]:
        out += i*m[c]
        i *= 5
    return out

def to_SNAFU(num):
    s = ""
    while num != 0:
        rem, num = num%5, num//5
        if rem == 0:
            s += "0"
        elif rem == 1:
            s += "1"
        elif rem == 2:
            s += "2"
        elif rem == 3:
            s += "="
            num += 1
        elif rem == 4:
            s += "-"
            num += 1
    return s[::-1]

def main():
    nums = [from_SNAFU(line) for line in open("25.dat").read().splitlines()]
    print(to_SNAFU(sum(nums)))

if __name__ == "__main__":
    main()
