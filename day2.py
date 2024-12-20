import aoc2024.aoc2024 as aoc

def part1(f):
    lines = f.readlines()

    safe = 0
    for line in lines:
        report = line.split(" ")
        i = 1
        incOrDec = 0
        isSafe = 1
        while i < len(report):
            diff = int(report[i -1]) - int(report[i])
            #Check if within range
            if(diff == 0 or abs(diff) > 3):
                isSafe = 0
                break
            #Check if inc or dec
            if(incOrDec == 0):
                incOrDec = diff
            else:
                if((incOrDec > 0 and diff < 0) or (incOrDec < 0 and diff > 0)):
                    isSafe = 0
                    break
            i += 1
        safe += isSafe
    print(safe)

def part2(f):
    raise NotImplementedError("Part 2 not implemented")

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())

