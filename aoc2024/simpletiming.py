#python3
import atexit
from time import time, strftime, localtime
from datetime import timedelta

def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

def endlogSimplified():
    end = time()
    elapsed = end-start
    print("Elapsed time:", secondsToStr(elapsed))

start = time()
atexit.register(endlogSimplified)
