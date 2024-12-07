import re

f = open("Puzzle3.txt", "r")
text = f.read()

ops = re.findall("mul\((\d+),\s*(\d+)\)", text)
#print(ops)

productSum = 0
for op in ops:
    productSum += (int(op[0]) * int(op[1]))

print(productSum)