def get_score(x, y):
    if x == 'A' and y == 'X':
        return 3
    if x == 'B' and y == 'Y':
        return 3
    if x == 'C' and y == 'Z':
        return 3
    if x == 'A' and y == 'Y':
        return 6
    if x == 'B' and y == 'Z':
        return 6
    if x == 'C' and y == 'X':
        return 6
    return 0

def rock_paper_scissors_part_one():
    scores = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    total_score = 0
    with open("file.txt") as file:
        for line in file:
            line = line.rstrip("\n")
            x, y = line.split()
            score = get_score(x, y)
            #print(f"Score of game {x} {y} is {score}")
            total_score += get_score(x, y) + scores[y]
        print(total_score)




def get_score(game):
    if game == 'X':
        return 0
    if game == 'Y':
        return 3
    if game == 'Z':
        return 6


WIN = 6
DRAW = 3
LOSE = 0

CHOOSE = {
        (WIN, 'A'): 2,
        (DRAW, 'A'): 1,
        (LOSE, 'A'): 3,
        (WIN, 'B'): 3,
        (DRAW, 'B'): 2,
        (LOSE, 'B'): 1,
        (WIN, 'C'): 1,
        (DRAW, 'C'): 3,
        (LOSE, 'C'): 2,
}


def rock_paper_scissors_part_two():
    total_score = 0
    with open("file.txt") as file:
        for line in file:
            line = line.rstrip("\n")
            x, y = line.split()
            score = get_score(y)
            total_score += score + CHOOSE[(score, x)]
        print(total_score)
