import aoc2024.aoc2024 as aoc
import re

def parse(f):
    machines = []
    for m in f.read().split("\n\n"):
        matches = re.findall(r"X[=+](\d+), Y[=+](\d+)", m)
        machines.append({
            "a": {"x": int(matches[0][0]), "y": int(matches[0][1])},
            "b": {"x": int(matches[1][0]), "y": int(matches[1][1])},
            "prize": {"x": int(matches[2][0]), "y": int(matches[2][1])}
        })
    return machines

def solve(ax, ay, bx, by, tx, ty):
    d = ax*by - ay*bx
    a = (tx*by - ty*bx)//d
    b = (ax*ty - ay*tx)//d
    if ax*a + bx*b == tx and ay*a + by*b == ty:
        return b + a*3
    return 0

def part1(f):
    machines = parse(f)
    tokens = 0
    for m in machines:
        tokens+=solve(m["a"]["x"], m["a"]["y"],m["b"]["x"], m["b"]["y"],m["prize"]["x"], m["prize"]["y"])
    print(tokens)

def part2(f):
    machines = parse(f)
    tokens = 0
    for m in machines:
        tokens+=solve(m["a"]["x"], m["a"]["y"],m["b"]["x"], m["b"]["y"],m["prize"]["x"] + 10000000000000, m["prize"]["y"] + 10000000000000)
    print(tokens)

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())