import re

def parse(filename:str) -> list[list]:
    lines = open(filename).readlines()
    result = []
    for line in lines:
        result.append([int(i) for i in re.findall(r'\d+', line)])
    return result

def doesFullyContainOther(assignment:list[int]) -> bool:
        elf1 = assignment[:2]
        elf2 = assignment[2:]
        if ((elf1[0] <= elf2[0] and elf1[1] >= elf2[1])
            or (elf1[0] >= elf2[0] and elf1[1] <= elf2[1])
            or (elf1[0] == elf2[0] and elf1[1] == elf2[1])
        ):
            print(elf1, elf2)
            return True
        return False
            
def countOverlap(assignments:list[list]) -> int:
    count = 0
    for assignment in assignments:
        # print(assignment)
        if doesFullyContainOther(assignment):
            count += 1
    return count

def solver_4_1():
    filename = "data.txt"
    result = countOverlap(parse(filename))
    print(result)


def checkOverlapAtAll(assignment:list[int]) -> bool:
    elf1 = assignment[:2]
    elf2 = assignment[2:]
    if ((elf2[0] <= elf1[1])
        and (elf1[0] <= elf2[1])):
        print(elf1, elf2)
        return True
    return False

def countOverlap2(assignments:list[list]):
    count = 0
    for assign in assignments:
        if checkOverlapAtAll(assign):
            count += 1
    return count

def solver_4_2():
    filename = "data.txt"
    result = countOverlap2(parse(filename))
    print(result)

if __name__ == '__main__':
    # solver_4_1()
    solver_4_2()