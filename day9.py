import aoc2024.aoc2024 as aoc
import itertools
from collections import Counter

emptyID = '.'

def parseMem(f):
    id = 0
    memory = []
    for pair in itertools.batched([int(i) for i in [*f.read()]], 2):
        memory.extend([id] * pair[0])
        if len(pair) == 2: memory.extend([emptyID] * pair[1])
        id+=1
    return memory

def orderMem(mem):
    cursor = 0
    for i in range(len(mem)-1, 0, -1):
        if mem[i] != emptyID:
            for j in range(cursor, i):
                cursor = j
                if(mem[j] == emptyID):
                    mem[j] = mem[i]
                    mem[i] = emptyID
                    break
        #print(*mem)

def checkSum(mem):
    total = 0
    for i in range(0, len(mem)):
        if mem[i] == ".":continue
        total+= i*mem[i]
    return total

def orderMem2(mem):
    counter = Counter(mem)
    for i in range(len(mem)-1, 0, -1):
        if mem[i] != emptyID:
            blockSize = counter[mem[i]]
            starti = None
            emptyCount = 0
            for j in range(0, i):
                if mem[j] == emptyID:
                    if emptyCount == 0:
                        starti = j
                        emptyCount+=1
                    else:
                        emptyCount+=1
                else:
                    starti = None
                    emptyCount = 0

                if emptyCount == blockSize:
                    for ei in range(starti, j+1):
                        mem[ei] = mem[i]
                    for bi in range(i, i-blockSize, -1):
                        mem[bi] = '.'
                    i-=blockSize
                    break

def part1(f):
    memory = parseMem(f)
    orderMem(memory)
    print(checkSum(memory))

def part2(f):
    memory = parseMem(f)
    orderMem2(memory)
    print(checkSum(memory))

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())