import re

def convertToCrate(crateLine:list[tuple]) -> list[list]:
    rowLen = len(crateLine[0]) # number of stacks, this is before transpose
    # for crate in crateLine:
    #     print("".join(crate))
    crates = list(row[i] for i in range(rowLen) for row in crateLine) # transpose crateLine list
    # print(len(crates))
    stacks = [crates[i:i+rowLen-1] for i in range(0, len(crates), rowLen-1)] # split into group of no of rows which is 1 less than the total stacks
    # print(stacks)
    result = [list(filter(lambda x:bool(x.strip()), stack[::-1])) for stack in stacks] # reversing the array and removing empty elements
    # for stack in result:
    #     print("".join(stack))
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
    # for crate in cratesLine:
    #     print("".join(crate))
    return convertToCrate(cratesLine), procedure    

def movingCrates(crates:list[list], procedure:tuple) -> list[list]:
    # procedure: 1, 2, 1 // move count, from stack, to stack
    for _ in range(procedure[0]):
        temp = crates[procedure[1]-1].pop() # removing item from from stack
        crates[procedure[2]-1].append(temp) # adding item in to stack
    return crates

def followProcedure(crates:list[list], procedures:list[tuple]) -> str:
    crateCopy = crates
    for procedure in procedures: # iterating through all procedures
        # print("Before procedure:", procedure)  # Debug before the procedure
        # drawCratesStacks(crateCopy)
        crateCopy = movingCrates(crateCopy, procedure)
        # print("After procedure:", procedure)  # Debug after the procedure
        # drawCratesStacks(crateCopy)
    
    topCrates = [stack[-1] for stack in crateCopy]
    temp = "".join([i[0] for i in [re.findall(r"\w", i) for i in topCrates]])
    # print(temp)
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
    result = followProcedure(crates, procedures)
    # print("Final result:", result)    # Debug final output
    print(result)

if __name__ == '__main__':
    solver_5_1()