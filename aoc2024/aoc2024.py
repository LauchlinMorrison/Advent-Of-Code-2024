import os.path
import tkinter.simpledialog as dialog
import aoc2024.configurator as configurator

def getInput():
    config = configurator.loadConfig()
    useExample = config["useExample"]
    day = config["day"]

    fileName = f"examples/Day{day}.pzl" if useExample else f"puzzleInputs/Day{day}.pzl"
    if not os.path.isfile(fileName):
        #text = input()
        text = dialog.askstring("Example not found" if useExample else "Puzzle not found", f"Enter day {day} example input:\n" if useExample else f"Enter day {day} puzzle input:\n")
        if text != None:
            f = open(fileName, "w")
            f.write(text)
            f.close()
    return open(fileName, "r")

def run(part1, part2):
    config = configurator.loadConfig()
    part = config["part"]

    if part == 1: part1(getInput())
    if part == 2: part2(getInput())

def part():
    return configurator.loadConfig()["part"]

def generatenewDay(day):
    print("Generating new day")
    code = '''import aoc2024.aoc2024 as aoc

def part1(f):
    raise NotImplementedError("Part 1 not implemented")

def part2(f):
    raise NotImplementedError("Part 2 not implemented")

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())'''


print("Loaded aoc")