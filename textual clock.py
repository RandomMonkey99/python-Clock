import time
from time import strftime
from time import sleep
import os

def time():
    string=strftime('%A %D %H:%M:%S: %p')
    print(string)
    sleep(1.00)
    os.system("cls")
    time()


time()
