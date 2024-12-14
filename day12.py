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

def getRegions(grid):
    plots = {}
    regions = {}
    regionID = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            region = checkNeighbours(x, y, grid, plots, regionID, grid[y][x])
            if len(region) > 0: regions[regionID] = region
            regionID+=1
    return regions

def removeSidePieceFromDictRecursively(dict, k, direction):
    if k in dict and direction in dict[k]:
        xy = [int(i) for i in k.split(",")]
        dict[k].remove(direction)
        if len(dict[k]) == 0: del dict[k]
        if direction == "Top" or direction == "Bot":
            removeSidePieceFromDictRecursively(dict, f"{xy[0]-1},{xy[1]}", direction)
            removeSidePieceFromDictRecursively(dict, f"{xy[0]+1},{xy[1]}", direction)
        elif direction == "Lft" or direction == "Rht":
            removeSidePieceFromDictRecursively(dict, f"{xy[0]},{xy[1]-1}", direction)
            removeSidePieceFromDictRecursively(dict, f"{xy[0]},{xy[1]+1}", direction)
        else:
            raise(Exception("What?!"))

def part1(f):
    grid = [[*l]for l in f.read().split()]
    regions = getRegions(grid)

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
        total+=len(v)*fences
    print(total)

def part2(f):
    grid = [[*l]for l in f.read().split()]
    regions = getRegions(grid)

    total = 0
    for v in regions.values():
        fences = {}
        for i in v:
            x = i[0]
            y = i[1]
            if not inBounds(x, y-1, grid) or not grid[y-1][x] == i[2]:
                if f"{x},{y}" in fences: fences[f"{x},{y}"].append("Top")
                else: fences[f"{x},{y}"] = ["Top"]
            if not inBounds(x, y+1, grid) or not grid[y+1][x] == i[2]:
                if f"{x},{y}" in fences: fences[f"{x},{y}"].append("Bot")
                else: fences[f"{x},{y}"] = ["Bot"]
            if not inBounds(x-1, y, grid) or not grid[y][x-1] == i[2]:
                if f"{x},{y}" in fences: fences[f"{x},{y}"].append("Lft")
                else: fences[f"{x},{y}"] = ["Lft"]
            if not inBounds(x+1, y, grid) or not grid[y][x+1] == i[2]:
                if f"{x},{y}" in fences: fences[f"{x},{y}"].append("Rht")
                else: fences[f"{x},{y}"] = ["Rht"]

        fenceSides = 0
        while(len(fences) > 0):
            key, val = next(iter(fences.items()), None)
            removeSidePieceFromDictRecursively(fences, key, val[0])
            fenceSides+=1
        total+=len(v)*fenceSides
    print(total)

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())