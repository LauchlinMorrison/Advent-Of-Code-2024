import aoclib.loader as loader
import itertools

calibration = [l.split(": ") for l in loader.getInput().readlines()]
for i in calibration:
    i[0] = int(i[0])
    i[1] = list(map(int,i[1].split()))


def checkCalibration(answer, numbers):
    for permutation in itertools.product(["*", "+"], repeat=len(numbers)-1):
        total = numbers[0]
        for i in range(len(permutation)):
            if permutation[i] == "*":
                total *= numbers[i+1]
            elif permutation[i] == "+":
                total += numbers[i+1]
        if total == answer: return True
    return False

runningTotal = 0
for c in calibration:
    if checkCalibration(c[0], c[1]): runningTotal+=c[0]

print(runningTotal)