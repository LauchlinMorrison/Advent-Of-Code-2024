import os.path
import json
from tkinter import *
from tkinter import ttk

configFileName = 'config.json'

def generateConfig():
    data = {
        "day": 1,
        "part": 1,
        "useExample": True,
        "profilerEnabled": False,
        "session_key": "null",
    }

    with open(configFileName, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def loadConfig():
    if not os.path.isfile(configFileName): 
        print("Config file not found. Generating default config.")
        generateConfig()
    with open(configFileName) as f:
        return json.load(f)

def generateNewDay(day):
    with open(f"day{day}.py", "w") as f:
        f.write('''import aoc2024.aoc2024 as aoc

def part1(f):
    raise NotImplementedError("Part 1 not implemented")

def part2(f):
    raise NotImplementedError("Part 2 not implemented")

part1(aoc.getInput()) if aoc.part() == 1 else part2(aoc.getInput())''')

def generateNextDay():
    from os import listdir
    from os.path import isfile, join
    import re
    lst = []
    for name in [f for f in listdir(".") if isfile(join('.', f))]:
        result = re.search("^day(\\d+).py$", name)
        if result:
            lst.append(int(result.group(1)))    
    lst.sort(reverse=True)
    daynum = lst[0] + 1
    generateNewDay(daynum)
    print(f"Generated day{daynum}.py")

def save():
    for k, v in settingsDict.items():
        config[k] = v.get()
    
    with open(configFileName, "w", encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=4)

# Will auto save when a checkbox is toggled.
def onChecked():
    save()

def launch():
    global config
    config = loadConfig()
    global settingsDict
    settingsDict = {}
    
    root = Tk()
    root.title("APC2024 Config")

    frame = ttk.Frame(root, padding="12 12 12 12")
    frame.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    row = 1
    for item in config:
        ttk.Label(frame, text=item).grid(column=0, row=row, sticky=W)
        value = config[item]
        if isinstance(value, bool):
            settingsDict[item] = BooleanVar()
            settingsDict[item].set(value)
            checkbox = ttk.Checkbutton(frame, command=onChecked, variable=settingsDict[item], onvalue=True, offvalue=False)
            checkbox.grid(column=1, row=row, sticky=(W, E))
        else:
            settingsDict[item] = StringVar()
            settingsDict[item].set(value)
            entry = ttk.Entry(frame, textvariable=settingsDict[item])
            entry.grid(column=1, row=row, sticky=(W, E))
        row+=1
    
    ttk.Button(frame, text="Save", command=save).grid(column=3, row=row, sticky=W)
    ttk.Button(frame, text="Generate Day", command=generateNextDay).grid(column=3, row=1, sticky=W)

    for child in frame.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    #root.bind("<Return>", None)

    root.mainloop()