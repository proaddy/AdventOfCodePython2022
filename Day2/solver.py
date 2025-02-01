def parse(filename:str) -> list[str]:
    lines = open(filename).readlines()
    rounds = []
    for line in lines:
        rounds.append(line.strip())
    return rounds

def find_score(rounds:list[str]) -> int:
    '''
        rock(A) - rock(X) - 1
        paper(B) - paper(Y) - 2
        scissor(C) - scissor(Z) - 3

        win = 6
        draw = 3
        loss = 0

        opponent me = outcome + shape
    '''
    pattern = {
        'A X':3 + 1,
        'A Y':6 + 2,
        'A Z':0 + 3,
        'B X':0 + 1,
        'B Y':3 + 2,
        'B Z':6 + 3,
        'C X':6 + 1,
        'C Y':0 + 2,
        'C Z':3 + 3,
    }
    total = 0
    for rnd in rounds:
        total += pattern[rnd]
    return total

def what_shape_to_choose(rounds:list[str]):
    '''
    X - lose
    Y - draw
    Z - win

    rock(A) - 1
    paper(B) - 2
    scissor(C) - 3

    opponent outcome = outcome + shape
    '''
    pattern = {
        'A X':0 + 3,
        'A Y':3 + 1,
        'A Z':6 + 2,
        'B X':0 + 1,
        'B Y':3 + 2,
        'B Z':6 + 3,
        'C X':0 + 2,
        'C Y':3 + 3,
        'C Z':6 + 1,
    }
    total = 0
    for rnd in rounds:
        total += pattern[rnd]
    return total

def solver_2_1():
    filename = "data.txt"
    result = find_score(parse(filename))
    print("Total -> ", result)

def solver_2_2():
    filename = "data.txt"
    result = what_shape_to_choose(parse(filename))
    print("Result -> ", result)

if __name__ == '__main__':
    # solver_2_1()
    solver_2_2()