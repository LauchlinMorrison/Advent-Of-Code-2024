import aoc2024.aoc2024 as aoc

def inBounds(x, y, grid):
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def checkNeighbours(x, y, grid, plots, regionID, char):
    region = []
    if inBounds(x, y, grid) and char == grid[y][x] and f"{x},{y}" not in plots:
        plots[f"{x},{y}"] = regionID
        region.append([x,y, grid[y][x]])
        region.extend(checkNeighbours(x, y-1, grid, plots, regionID, char))
        region.extend(checkNeighbours(x, y+1, grid, plots, regionID, char))
        region.extend(checkNeighbours(x-1, y, grid, plots, regionID, char))
        region.extend(checkNeighbours(x+1, y, grid, plots, regionID, char))
    return region

def part1(f):
    grid = [[*l]for l in f.read().split()]
    plots = {}
    regions = {}
    regionID = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            region = checkNeighbours(x, y, grid, plots, regionID, grid[y][x])
            if len(region) > 0: regions[regionID] = region
            regionID+=1

    total = 0
    for v in regions.values():
        fences = 0
        for i in v:
            x = i[0]
            y = i[1]
            if not inBounds(x, y-1, grid) or not grid[y-1][x] == i[2]: fences+=1
            if not inBounds(x, y+1, grid) or not grid[y+1][x] == i[2]: fences+=1
            if not inBounds(x-1, y, grid) or not grid[y][x-1] == i[2]: fences+=1
            if not inBounds(x+1, y, grid) or not grid[y][x+1] == i[2]: fences+=1
        tmp = len(v)*fences
        total+=len(v)*fences
    print(total)

def part2(f):
    raise NotImplementedError("Part 2 not implemented")

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())