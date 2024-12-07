import aoc2024.aoc2024 as aoc

def parseInputToSortedLists(f):
    lines = f.readlines()
    list1 = []
    list2 = []
    result = 0

    for line in lines:
        l = line.replace("\n", "").split("   ")
        list1.append(int(l[0]))
        list2.append(int(l[1]))

    list1.sort()
    list2.sort()

    return [list1, list2]

def part1(f):
    list1, list2 = [*parseInputToSortedLists(f)]
    result = 0
    i = 0
    while i < len(list1):
        result += abs(list1[i] - list2[i])
        i += 1
    print(result)

def part2(f):
    list1, list2 = [*parseInputToSortedLists(f)]
    result = 0
    i = 0
    while i < len(list1):
        result += list1[i] * list2.count(list1[i])
        i += 1
    print(result)

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())