import aoc2024.aoc2024 as aoc
import re
from functools import reduce
from operator import mul

#gridSizeX = 11
#gridSizeY = 7
gridSizeX = 101
gridSizeY = 103

centerX = gridSizeX//2
centerY = gridSizeY//2

def part1(f):
    #robots = [re.match("p=([+-]?\d+),([+-]?\d+) v=([+-]?\d+),([+-]?\d+)", r) for r in f.readlines()]
    robots = []
    for line in f.readlines():
        match = re.match("p=([+-]?\\d+),([+-]?\\d+) v=([+-]?\\d+),([+-]?\\d+)", line)
        robots.append({"x": int(match[1]), "y": int(match[2]), "vx": int(match[3]), "vy": int(match[4])})
    
    quad = [0,0,0,0]
    for robot in robots:
        robot["x"] = (robot["x"] + robot["vx"]*100)%gridSizeX
        robot["y"] = (robot["y"] + robot["vy"]*100)%gridSizeY

        if robot["x"] < centerX and robot["y"] < centerY:
            quad[0]+=1
        if robot["x"] > centerX and robot["y"] < centerY:
            quad[1]+=1
        if robot["x"] < centerX and robot["y"] > centerY:
            quad[2]+=1
        if robot["x"] > centerX and robot["y"] > centerY:
            quad[3]+=1
    
    print(reduce(mul, quad))

def part2(f):
    robots = []
    for line in f.readlines():
        match = re.match("p=([+-]?\\d+),([+-]?\\d+) v=([+-]?\\d+),([+-]?\\d+)", line)
        robots.append({"x": int(match[1]), "y": int(match[2]), "vx": int(match[3]), "vy": int(match[4])})
    
    for iteration in range(99, 10000, 101):
        grid = [["." for x in range(gridSizeX)] for y in range(gridSizeY)]
        for robot in robots:
            grid[(robot["y"] + robot["vy"]*iteration)%gridSizeY][(robot["x"] + robot["vx"]*iteration)%gridSizeX] = "*"
        for l in grid:
            print(*l)
        print(iteration)
        print("")
        #8179
    



part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())