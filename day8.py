import aoc2024.aoc2024 as aoc
import itertools
from collections import defaultdict
import numpy as np

def parseAntenas(f):
    d = defaultdict(list)
    y=0
    for l in f.readlines():
        x=0
        for c in [*l]:
            if c!='.' and c!= "\n":
                d[c].append(np.array([x,y]))
            x+=1
        y+=1
    gs = [x, y]
    return d, gs

def visualizeGrid(antinodes, size):
    grid = [['.']*size[0] for i in range(size[1])]
    for k, v in antinodes.items():
        for a in v:
            grid[a[1]][a[0]] = k
    gridString = ""
    for row in grid:
        gridString += "".join(row) + "\n"
    print(gridString)


def part1(f):
    antenas, gridSize = parseAntenas(f)
    antinodes = defaultdict(list)
    antinodessimple = {}
    for k, v in antenas.items():
        for i in range(len(v)-1):
            for j in range(i+1, len(v)):
                slope = v[j]-v[i]
                antis = [v[i]-slope, v[j]+slope]
                for a in antis:
                    if a[0] in range(0, gridSize[0]) and a[1] in range(0, gridSize[1]):
                        antinodes[k].append(a)
                        antinodessimple[f"{a}"] = 0
    visualizeGrid(antinodes, gridSize)
    print(len(antinodessimple))

def part2(f):
    antenas, gridSize = parseAntenas(f)
    antinodes = defaultdict(list)
    antinodessimple = {}
    for k, v in antenas.items():
        for i in range(len(v)-1):
            for j in range(i+1, len(v)):
                slope = v[j]-v[i]
                newAnti = v[i]*[1,1]
                while(newAnti[0] in range(0, gridSize[0]) and newAnti[1] in range(0, gridSize[1])):
                    antinodessimple[f"{newAnti}"] = 0
                    newAnti-=slope
                newAnti = v[j]*[1,1]
                while(newAnti[0] in range(0, gridSize[0]) and newAnti[1] in range(0, gridSize[1])):
                    antinodessimple[f"{newAnti}"] = 0
                    newAnti+=slope
    visualizeGrid(antinodes, gridSize)
    print(len(antinodessimple))

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())