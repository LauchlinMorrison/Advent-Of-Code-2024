import aoclib.loader as loader

lines = open(loader.input("5"), "r").readlines()
lines = [l.replace("\n", "") for l in lines]

total = 0
rules = {}
updates = []

blankLineIndex = lines.index("")
for rule in lines[:blankLineIndex]:
    kv = [int(x) for x in rule.split("|")]
    if(rules.get(kv[0]) == None):
        rules[kv[0]] = [kv[1]]
    else:
        val = rules.get(kv[0])
        val.append(kv[1])
        rules[kv[0]] = val
    
for update in lines[blankLineIndex+1:]:
    updates.append([int(x) for x in update.split(",")])

for update in updates:
    isGood = True

    for i in range(0, len(update)-1):
        r = rules.get(update[i])
        if r == None:
            isGood = False
            break
        s = set(r)
        num = len(s.intersection(update[i:len(update)]))
        if(num != len(update)-i-1):
            isGood = False
            break
    if isGood: total+=update[(len(update)-1)//2]
    #print(total)

print(f"Number: {total}")