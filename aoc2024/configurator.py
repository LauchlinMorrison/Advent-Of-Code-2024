import os.path
import json

configFileName = 'config.json'

def generateConfig():
    data = {
        "useExample": True,
        "day": 1,
        "part": 1,
        "session_key": "null",
        "profilerEnabled": True
    }

    with open(configFileName, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def loadConfig():
    if not os.path.isfile(configFileName): 
        print("Config file not found. Generating default config.")
        generateConfig()
    with open(configFileName) as f:
        return json.load(f)