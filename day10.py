import aoc2024.aoc2024 as aoc
from collections import Counter

def searchTrailhead(grid, x, y, lastNum, ends):
    if x not in range(0, len(grid[0])) or y not in range(0, len(grid)): return
    if grid[y][x] == lastNum+1:
        if grid[y][x] == 9:
            ends.append(tuple([x,y]))
        else:
            searchTrailhead(grid, x+1, y, grid[y][x], ends)
            searchTrailhead(grid, x-1, y, grid[y][x], ends)
            searchTrailhead(grid, x, y+1, grid[y][x], ends)
            searchTrailhead(grid, x, y-1, grid[y][x], ends)

def part1(f):
    grid = [[int(i) for i in list(l)] for l in f.read().split()]
    trailheads = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == 0:
                endLocations =[]
                searchTrailhead(grid, x, y, -1, endLocations)
                trailheads+=len(Counter(endLocations).keys())
    print(trailheads)

def part2(f):
    grid = [[int(i) for i in list(l)] for l in f.read().split()]
    trailheads = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == 0:
                endLocations =[]
                searchTrailhead(grid, x, y, -1, endLocations)
                trailheads+=len(endLocations)
    print(trailheads)

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())