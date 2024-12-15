import aoc2024.aoc2024 as aoc

def printGrid(grid):
    for r in grid:
        print(*r)

def parseInput(f):
    gridStr, instructionStr = f.read().split("\n\n")
    grid = [[*line] for line in gridStr.split()]
    instructions = [*instructionStr.replace("\n", "")]
    return grid, instructions

def findRobot(grid):
    for row in grid:
        if "@" in row:
            return [row.index("@"), grid.index(row)]
        
def executeInstruction(grid, robotLoc, i):
    if i == "^":
        if tryMove(grid, robotLoc[0], robotLoc[1], 0, -1): robotLoc[1]-=1 
    elif i == "v":
        if tryMove(grid, robotLoc[0], robotLoc[1], 0, 1): robotLoc[1]+=1
    elif i == "<":
        if tryMove(grid, robotLoc[0], robotLoc[1], -1, 0): robotLoc[0]-=1
    elif i == ">":
        if tryMove(grid, robotLoc[0], robotLoc[1], 1, 0): robotLoc[0]+=1
    else:
        raise(Exception(f"Invalid Instruction: {i}"))

def tryMove(grid, x, y, xmove, ymove):
    targetChar = grid[y+ymove][x+xmove]
    if targetChar == "#":
        return False
    if targetChar == ".":
        grid[y+ymove][x+xmove] = grid[y][x]
        grid[y][x] = "."
        return True
    if targetChar == "O":
        if tryMove(grid, x+xmove, y+ymove, xmove, ymove):
            grid[y+ymove][x+xmove] = grid[y][x]
            grid[y][x] = "."
            return True
        else: 
            return False
    raise(Exception("Invalid move?!"))

def calculateGPSSystem(grid, character):
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == character:
                total += 100*y + x
    return total

def expandGrid(grid):
    for row in grid:
        newRow = []
        for c in row:
            if c == "@":
                newRow.extend(["@", "."])
            elif c == "O":
                newRow.extend(["[", "]"])
            else:
                newRow.extend([c,c])
        grid[grid.index(row)] = newRow

def executeInstruction2(grid, robotLoc, i):
    #x, y, char1, x2, y2, char2
    moveQueue =[]
    if i == "^":
        if queueMove(grid, robotLoc[0], robotLoc[1], 0, -1, moveQueue):
            executeQueue(grid, moveQueue)
            robotLoc[1]-=1
    elif i == "v":
        if queueMove(grid, robotLoc[0], robotLoc[1], 0, 1, moveQueue):
            executeQueue(grid, moveQueue)
            robotLoc[1]+=1
    elif i == "<":
        if queueMove(grid, robotLoc[0], robotLoc[1], -1, 0, moveQueue):
            executeQueue(grid, moveQueue)
            robotLoc[0]-=1
    elif i == ">":
        if queueMove(grid, robotLoc[0], robotLoc[1], 1, 0, moveQueue):
            executeQueue(grid, moveQueue)
            robotLoc[0]+=1
    else:
        raise(Exception(f"Invalid Instruction: {i}"))
    
    
    
def queueMove(grid, x, y, xmove, ymove, queue):
    currChar = grid[y][x]
    targetChar = grid[y+ymove][x+xmove]
    move = [x+xmove, y+ymove, x, y]
    if targetChar == "#":
        return False
    if targetChar == ".":
        if move not in queue: queue.append(move)
        return True
    # if targetChar == "O":
    #     if queueMove(grid, x+xmove, y+ymove, xmove, ymove, queue):
    #         queue.append([x+xmove, y+ymove, x, y])
    #         return True
    #     else: 
    #         return False
    if (targetChar == "[" or targetChar == "]") and xmove != 0:
        if queueMove(grid, x+xmove, y+ymove, xmove, ymove, queue):
            if move not in queue: queue.append(move)
            return True
        else: 
            return False
    if (targetChar == "[" or targetChar == "]") and ymove != 0:
        if targetChar == "[":
            if queueMove(grid, x+xmove, y+ymove, xmove, ymove, queue) and queueMove(grid, x+xmove+1, y+ymove, xmove, ymove, queue):
                if move not in queue: queue.append(move)
                return True
            else: 
                return False
        if targetChar == "]":
            if queueMove(grid, x+xmove, y+ymove, xmove, ymove, queue) and queueMove(grid, x+xmove-1, y+ymove, xmove, ymove, queue):
                if move not in queue: queue.append(move)
                return True
            else: 
                return False

    raise(Exception("Invalid move?!"))

def executeQueue(grid, queue):
    for move in queue:
        tmpchar = grid[move[1]][move[0]]
        grid[move[1]][move[0]] = grid[move[3]][move[2]]
        grid[move[3]][move[2]] = tmpchar

def part1(f):
    grid, instrucitons = parseInput(f)
    robotLoc = findRobot(grid)
    print("Start:")
    printGrid(grid)

    for i in instrucitons:
        executeInstruction(grid, robotLoc, i)
        #print(f"Ins: {i}")
        #printGrid(grid)
    
    print(calculateGPSSystem(grid, "O"))

def part2(f):
    grid, instrucitons = parseInput(f)
    expandGrid(grid)
    robotLoc = findRobot(grid)
    #print("Start:")
    #printGrid(grid)

    for i in instrucitons:
        executeInstruction2(grid, robotLoc, i)
        #print(f"Ins: {i}")
        #printGrid(grid)
    
    print(calculateGPSSystem(grid, "["))

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())