f = open("PuzzleInputs/RussellDay2Input.txt", "r")
lines = f.readlines()

safe = 0

def isReportSafe(report):
    i = 1
    incOrDec = 0
    isSafe = 1
    while i < len(report):
        diff = int(report[i -1]) - int(report[i])
        #Check if within range
        if(diff == 0 or abs(diff) > 3):
            return False
        #Check if inc or dec
        if(incOrDec == 0):
            incOrDec = diff
        else:
            if((incOrDec > 0 and diff < 0) or (incOrDec < 0 and diff > 0)):
               return False
        i += 1
    return True

def tryRemoveOne(report):
    i = 0
    while i < len(report):
        list = report.copy()
        del list[i]
        if(isReportSafe(list)):
            return True
        i += 1
    return False

#index = 1
for line in lines:
    report = line.split(" ")
    if(isReportSafe(report)):
        #safe += 1
        print(index)
    elif(tryRemoveOne(report)):
        safe += 1
        #print(index)
    #index += 1
print(safe)