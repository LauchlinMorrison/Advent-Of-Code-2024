import os.path
import tkinter.simpledialog as dialog

#import aoclib.simpletiming
import aoclib.configurator as configurator

def getInput():
    config = configurator.loadConfig()
    useExample = config["useExample"]
    day = config["day"]
    
    fileName = f"Examples/Day{day}.pzl" if useExample else f"PuzzleInputs/Day{day}.pzl"
    if not os.path.isfile(fileName):
        #text = input()
        text = dialog.askstring("Example not found" if useExample else "Puzzle not found", f"Enter day {day} example input:\n" if useExample else f"Enter day {day} puzzle input:\n")
        if text != None:
            f = open(fileName, "w")
            f.write(text)
            f.close()
    return open(fileName, "r")

getInput()