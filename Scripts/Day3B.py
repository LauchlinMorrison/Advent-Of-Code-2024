import re

f = open("PuzzleInputs/Day3.txt", "r")
text = f.read()

ops = re.findall("mul\((\d+),\s*(\d+)\)|(do\(\))|(don\'t\(\))", text)
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