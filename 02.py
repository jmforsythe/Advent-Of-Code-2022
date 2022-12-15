def get_score1(a, b):
    score = 0
    if b == "X":
        score = 1
        if a == "C":
            score += 6
        elif a == "A":
            score += 3
    elif b == "Y":
        score = 2
        if a == "A":
            score += 6
        elif a == "B":
            score += 3
    elif b == "Z":
        score = 3
        if a == "B":
            score += 6
        elif a == "C":
            score += 3
    return score

def get_score2(a, b):
    score = 0
    if b == "X":
        score = 0
        if a == "A":
            score += 3
        elif a == "B":
            score += 1
        elif a == "C":
            score += 2
    elif b == "Y":
        score = 3
        if a == "A":
            score += 1
        elif a == "B":
            score += 2
        elif a == "C":
            score += 3
    elif b == "Z":
        score = 6
        if a == "A":
            score += 2
        elif a == "B":
            score += 3
        elif a == "C":
            score += 1
    return score

score1 = 0
score2 = 0

with open("2.dat") as f:
    for line in f:
        a, b = line.rstrip().split(" ")
        score1 += get_score1(a,b)
        score2 += get_score2(a,b)

print(score1, score2)
