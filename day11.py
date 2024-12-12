import aoc2024.aoc2024 as aoc

def blink(stones, times):
    for _ in range(times):
        stones2 = []
        for s in stones:
            if s == 0:
                stones2.append(1)
            elif len(f"{s}")%2 == 0:
                stonestr = str(s)
                stonestrMidpoint = len(stonestr)//2
                stones2.append(int(stonestr[:stonestrMidpoint]))
                stones2.append(int(stonestr[stonestrMidpoint:]))
            else:
                stones2.append(s*2024)
        stones = stones2
    return stones

def blink2(stones, times):
    for _ in range(times):
        newStones = {}
        for k, v in stones.items():
            newKeys = []
            if k == 0:
                newKeys.append(1)
            elif len(f"{k}")%2 == 0:
                stonestr = str(k)
                stonestrMidpoint = len(stonestr)//2
                newKeys.append(int(stonestr[:stonestrMidpoint]))
                newKeys.append(int(stonestr[stonestrMidpoint:]))
            else:
                newKeys.append(k*2024)
            for nk in newKeys:
                if nk in newStones: newStones[nk]+=v
                else: newStones[nk] = v
        stones = newStones
    return stones

def part1(f):
    stones = [int(i) for i in f.read().split()]
    stones = blink(stones, 25)
    print(len(stones))

def part2(f):
    stones = {k:1 for k in [int(i) for i in f.read().split()]}
    stones = blink2(stones, 75)
    print(sum(stones.values()))

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())




