import aoclib.loader as loader
import operator
import itertools

def inbounds(location, grid):
    if location[0] < 0 or location[0] > len(grid[0])-1 or location[1] < 0 or location[1] > len(grid)-1:
        return False
    return True

grid = [list(l) for l in loader.getInput().read().split()]
guardIndex = [c for l in grid for c in l].index("^")
start = [guardIndex%len(grid) ,guardIndex//len(grid[0])]
cursor = start
directions = [[0,-1],[1,0],[0,1],[-1,0]]
direction = 0
locationHistory = {}
while(inbounds(cursor, grid)):
    locationHistory[f"{cursor}"] = cursor
    stepCursor = list(map(operator.add, cursor, directions[direction%len(directions)]))
    if inbounds(stepCursor, grid) and grid[stepCursor[1]][stepCursor[0]] == "#":
        direction+=1
    else:
        cursor = stepCursor
    #print("\033[H\033[J", end="")
    #print("\n".join(map("".join, grid)))
flat = list(itertools.chain(*grid))
print(flat.count("*"))

loops = 0
for key, location in locationHistory.items():
    currRun = {}
    cursor = start
    direction = 0
    grid[location[1]][location[0]] = "O"
    while(inbounds(cursor, grid)):
        
        #There might be a bug if we remove this.
        grid[cursor[1]][cursor[0]] = "*"

        stepCursor = list(map(operator.add, cursor, directions[direction%len(directions)]))
        if inbounds(stepCursor, grid) and (grid[stepCursor[1]][stepCursor[0]] == "#" or grid[stepCursor[1]][stepCursor[0]] == "O"):
            direction+=1
        else:
            if f"{cursor}{direction%len(directions)}" in currRun:
                loops+=1
                break
            else:
                currRun[f"{cursor}{direction%len(directions)}"] = ""
            cursor = stepCursor

        #print("\033[H\033[J", end="")
        #print("\n".join(map("".join, grid)))
        

    tmp = 0
    #For display only
    for l in grid:
        for i, s in enumerate(l):
            if s == "*" or s == "O":
                l[i] = "."


print(loops)