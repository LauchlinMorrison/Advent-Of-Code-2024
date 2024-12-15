import aoc2024.aoc2024 as aoc
import re

def part1(f):
    ops = re.findall("mul\((\d+),\s*(\d+)\)", f.read())
    #print(ops)
    productSum = 0
    for op in ops:
        productSum += (int(op[0]) * int(op[1]))
    print(productSum)

def part2(f):
    ops = re.findall("mul\((\d+),\s*(\d+)\)|(do\(\))|(don\'t\(\))", f.read())
    print(ops)
    productSum = 0
    doDontFlag = True
    for op in ops:
        if(op[2] == "do()"):
            doDontFlag = True
        elif(op[3] == "don't()"):
            doDontFlag = False
        else:
            if(doDontFlag):
                productSum += (int(op[0]) * int(op[1]))
    print(productSum)

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())