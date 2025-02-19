import re

def convertToCrate(crate_line:list[tuple]) -> list[list]:
    rowLen = len(crate_line[0]) # number of stacks, before transpose
    crates = list(row[i] for i in range(rowLen) for row in crate_line) # transpose crate_line list
    stacks = [crates[i:i+rowLen-1] for i in range(0, len(crates), rowLen-1)] # group by row
    result = [list(filter(lambda x:bool(x.strip()), stack[::-1])) for stack in stacks] # reverse and clean stack
    return result

def parse(filename:str) -> tuple[list]:
    lines = open(filename).readlines()
    cratesLine = []
    procedure = []
    for line in lines:
        if "[" in line:
            cratesLine.append(tuple(line[i:i+3] for i in [j for j in range(0, len(line), 4)]))
        if "move" in line:
            procedure.append(tuple(map(int, re.findall(r"\d+", line))))
    return convertToCrate(cratesLine), procedure    

def movingCrates_1(crates:list[list], procedure:tuple) -> list[list]:
    # procedure: 1, 2, 1 // move count, from stack, to stack
    temp = []
    for _ in range(procedure[0]):
        temp = crates[procedure[1]-1].pop() # removing item from from stack
        crates[procedure[2]-1].append(temp) # adding item in to stack
    return crates

def movingCrates_2(crates:list[list], procedure:tuple) -> list[list]:
    # procedure: 1, 2, 1 // move count, from stack, to stack
    temp = []
    for _ in range(procedure[0]):
        temp.append(crates[procedure[1]-1].pop()) # removing item from from stack
    temp.reverse() # reversing temp stack
    crates[procedure[2]-1].extend(temp) # adding item in to stack
    return crates

def followProcedure(crates:list[list], procedures:list[tuple], how_to_move) -> str:
    crateCopy = crates
    for procedure in procedures: # iterating through all procedures
        # print("Before procedure:", procedure)  # Debug before the procedure
        # drawCratesStacks(crateCopy)
        crateCopy = how_to_move(crateCopy, procedure)
        # print("After procedure:", procedure)  # Debug after the procedure
        # drawCratesStacks(crateCopy)
    
    topCrates = [stack[-1] for stack in crateCopy]
    print(topCrates)
    temp = "".join([i[0] for i in [re.findall(r"\w", crate) for crate in topCrates]])
    return temp

def drawCratesStacks(crates:list[list]):
    for crate in crates:
        print("".join(crate))
    print()

def solver_5_1():
    filename = "data.txt"
    crates, procedures = parse(filename)
    # print("Initial crates:", crates)  # Debug initial crate state
    # print("Procedures:", procedures)  # Debug procedures
    result = followProcedure(crates, procedures, movingCrates_1)
    # print("Final result:", result)    # Debug final output
    print("Part 1 -> ", result)

def solver_5_2():
    filename = "data.txt"
    crates, procedures = parse(filename)
    result = followProcedure(crates, procedures, movingCrates_2)
    print("Part 2 -> ", result)

if __name__ == '__main__':
    solver_5_1()
    solver_5_2()