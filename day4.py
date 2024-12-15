import aoc2024.aoc2024 as aoc

def findAllOccurences(y, x, maxY, maxX, matrix):
    total = 0
    if checkN(y, x, maxY, maxX, matrix): total+=1
    if checkNE(y, x, maxY, maxX, matrix): total+=1
    if checkE(y, x, maxY, maxX, matrix): total+=1
    if checkSE(y, x, maxY, maxX, matrix): total+=1
    if checkS(y, x, maxY, maxX, matrix): total+=1
    if checkSW(y, x, maxY, maxX, matrix): total+=1
    if checkW(y, x, maxY, maxX, matrix): total+=1
    if checkNW(y, x, maxY, maxX, matrix): total+=1
    return total

def checkN(y, x, maxY, maxX, matrix):
    if y < 3: return False
    if matrix[y-1][x] == 'M' and matrix[y-2][x] == 'A' and matrix[y-3][x] == 'S': return True

def checkS(y, x, maxY, maxX, matrix):
    if y > maxY-3: return False
    if matrix[y+1][x] == 'M' and matrix[y+2][x] == 'A' and matrix[y+3][x] == 'S': return True

def checkW(y, x, maxY, maxX, matrix):
    if x < 3: return False
    if matrix[y][x-1] == 'M' and matrix[y][x-2] == 'A' and matrix[y][x-3] == 'S': return True

def checkE(y, x, maxY, maxX, matrix):
    if x > maxX-3: return False
    if matrix[y][x+1] == 'M' and matrix[y][x+2] == 'A' and matrix[y][x+3] == 'S': return True

def checkNE(y, x, maxY, maxX, matrix):
    if y < 3: return False
    if x > maxX-3: return False
    if matrix[y-1][x+1] == 'M' and matrix[y-2][x+2] == 'A' and matrix[y-3][x+3] == 'S': return True

def checkNW(y, x, maxY, maxX, matrix):
    if y < 3: return False
    if x < 3: return False
    if matrix[y-1][x-1] == 'M' and matrix[y-2][x-2] == 'A' and matrix[y-3][x-3] == 'S': return True

def checkSE(y, x, maxY, maxX, matrix):
    if y > maxY-3: return False
    if x > maxX-3: return False
    if matrix[y+1][x+1] == 'M' and matrix[y+2][x+2] == 'A' and matrix[y+3][x+3] == 'S': return True

def checkSW(y, x, maxY, maxX, matrix):
    if y > maxY-3: return False
    if x < 3: return False
    if matrix[y+1][x-1] == 'M' and matrix[y+2][x-2] == 'A' and matrix[y+3][x-3] == 'S': return True

def findMAS(y, x, maxY, maxX, matrix):
    if y < 1 or y > maxY-1 or x < 1 or x > maxX-1: return False

    if (((matrix[y-1][x-1] == 'M' and matrix[y+1][x+1] == "S") or 
        (matrix[y-1][x-1] == 'S' and matrix[y+1][x+1] == "M")) and
        ((matrix[y-1][x+1] == 'M' and matrix[y+1][x-1] == "S") or 
        (matrix[y-1][x+1] == 'S' and matrix[y+1][x-1] == "M"))): return True

def part1(f):
    lines = f.readlines()

    matrix = []
    for line in lines:
        matrix.append(list(line))

    #print(matrix)
    count = 0
    y = 0
    while y < len(matrix):
        x = 0
        while x < len(matrix[y]):
            if(matrix[y][x] == 'X'):
                count += findAllOccurences(y, x, len(matrix)-1, len(matrix[y])-1, matrix)
            #print(matrix[y][x])
            x+=1
        y+=1
    print(f"Total: {count}")
    #print(matrix[1][1])

def part2(f):
    lines = f.readlines()

    matrix = []
    for line in lines:
        matrix.append(list(line))

    count = 0
    y = 0
    while y < len(matrix):
        x = 0
        while x < len(matrix[y]):
            if(matrix[y][x] == 'A'):
                if findMAS(y, x, len(matrix)-1, len(matrix[y])-1, matrix): count+=1
            x+=1
        y+=1
    print(f"Total: {count}")

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())

