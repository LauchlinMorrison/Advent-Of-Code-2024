import functools

rules, updates = open("PuzzleInputs/Day5.txt", "r").read().split("\n\n")
cmp = functools.cmp_to_key(lambda x, y: -(x+'|'+y in rules))

a = [0,0]
for page in updates.split():
    page = page.split(',')
    s = sorted(page, key=cmp)
    a[page!=s] += int(s[len(s)//2])
print(*a)

#Blatantly copied code. But I learned a lot in implementing and understanding what every little part is doing.