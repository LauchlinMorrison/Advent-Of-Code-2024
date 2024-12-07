import aoclib.loader as loader
import operator
import itertools

def inbounds(location, grid):
    if location[0] < 0 or location[0] > len(grid[0])-1 or location[1] < 0 or location[1] > len(grid)-1:
        return False
    return True

grid = [list(l) for l in loader.getInput().read().split()]
guardIndex = [c for l in grid for c in l].index("^")
cursor = [guardIndex%len(grid) ,guardIndex//len(grid[0])]
directions = [[0,-1],[1,0],[0,1],[-1,0]]
direction = 0
while(inbounds(cursor, grid)):
    grid[cursor[1]][cursor[0]] = "*"
    stepCursor = list(map(operator.add, cursor, directions[direction%len(directions)]))
    if inbounds(stepCursor, grid) and grid[stepCursor[1]][stepCursor[0]] == "#":
        direction+=1
    else:
        cursor = stepCursor
    #print("\033[H\033[J", end="")
    #print("\n".join(map("".join, grid)))
flat = list(itertools.chain(*grid))
print(flat.count("*"))