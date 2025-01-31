def parse(filename:str) -> list[int]:
    lines = open(filename).readlines()

    elf_list = []
    total = 0

    for line in lines:
        if line == '\n':
            elf_list.append(total)
            total = 0
            continue
        total += int(line)

    elf_list.append(total)
    return elf_list

def solver_1_1():
    filename = "data.txt"
    result = parse(filename)

    print("Part 1 -> ", max(result))


    result.sort()
    result.reverse()
    print("Part 2 -> ", result[0]+result[1]+result[2])

if __name__ == '__main__':
    solver_1_1()