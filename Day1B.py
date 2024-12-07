f = open("Puzzle1.txt", "r")
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


#Part 1
i = 0
while i < len(list1):
    result += abs(list1[i] - list2[i])
    i += 1
print(result)

#Part 2
result2 = 0
i = 0
while i < len(list1):
    result2 += list1[i] * list2.count(list1[i])
    i += 1

print(list1)
print(list2)
print(result2)