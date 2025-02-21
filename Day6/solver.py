def parse(filename:str) -> list[str]:
    lines = open(filename).readlines()
    return lines

def where_msg_starts(n, line:str) -> int:
    for i in range(len(line)-n):
        if len(set(line[i:i+n])) == n:
            return i+n

def read_lines(start_marker_length:int, lines:list[str]) -> int:
    temp = 0
    for line in lines:
        temp = where_msg_starts(start_marker_length, line)
        # print(temp)
    return temp

def solver_6_1():
    filename = "data.txt"
    result = read_lines(4, parse(filename))
    print(result)

def solver_6_2():
    filename = "data.txt"
    result = read_lines(14, parse(filename))
    print(result)

if __name__ == '__main__':
    solver_6_1()
    solver_6_2()