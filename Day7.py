import aoc2024.aoc2024 as aoc
import itertools

def findTotalCalibratedEntries(f, operations):
    calibration = [l.split(": ") for l in f.readlines()]
    for i in calibration:
        i[0] = int(i[0])
        i[1] = list(map(int,i[1].split()))

    runningTotal = 0
    for c in calibration:
        if checkCalibration(c[0], c[1], operations): runningTotal+=c[0]

    print(runningTotal)

def checkCalibration(answer, numbers, operations):
    for permutation in itertools.product(operations, repeat=len(numbers)-1):
        total = numbers[0]
        for i in range(len(permutation)):
            if permutation[i] == "*":
                total *= numbers[i+1]
            elif permutation[i] == "+":
                total += numbers[i+1]
            elif permutation[i] == "|":
                total = int(f"{total}" + f"{numbers[i+1]}")
        if total == answer: return True
    return False

def part1(f):
    findTotalCalibratedEntries(f, ["*", "+"])

def part2(f):
    findTotalCalibratedEntries(f, ["*", "+", "|"])

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())