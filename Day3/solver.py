import string
from typing import Generator  

# Common data
lowercase = {char:i+1 for i, char in enumerate(string.ascii_lowercase[:26])}
uppercase = {char:i+27 for i, char in enumerate(string.ascii_uppercase[:26])}

def parseGeneratorEachLine(filename: str) -> Generator[str, None, None]:
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

def sumOfPriority(items: Generator[str, None, None]) -> None:
    total = 0
    common = set()

    for item in items:
        mid = len(item)//2
        str1, str2 = set(item[:mid]), set(item[mid:])
        common = str1.intersection(str2)
        common = common.pop()
        if(common.isupper()):
            total += uppercase[common]
        else:
            total += lowercase[common]
    return total

def solver_3_1():
    filename = "data.txt"
    result = sumOfPriority(parseGeneratorEachLine(filename))
    print(result)

def parseGeneratorThreeLines(filename:str) -> Generator[str, None, None]:
    lines = open(filename).readlines()
    for i in range(0, len(lines), 3):
        yield lines[i:i+3]  

def findingBadges(items:Generator[str, None, None]) -> int:
    # print(next(items))
    total = 0
    for x in items:
        set1, set2, set3 = set(x[0].strip()), set(x[1].strip()), set(x[2].strip())

        temp1 = set1.intersection(set2)
        temp2 = temp1.intersection(set3)
        result = temp2.pop()
        # print(result)
        if(result.isupper()):
            total += uppercase[result]
        else:
            total += lowercase[result]
    return total

def solver_3_2():
    filename = "data.txt"
    result = findingBadges(parseGeneratorThreeLines(filename))
    print(result)

if __name__ == '__main__':
    # solver_3_1()
    solver_3_2()