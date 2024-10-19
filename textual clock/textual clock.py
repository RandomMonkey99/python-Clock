import time
from time import strftime
from time import sleep
import os
from termcolor import colored #before you have to install termcolor : pip install termcolor

def time():
    string=strftime('%A %D %H:%M:%S: %p')
    print(colored(string, "green"))#you can also replace with another color
    sleep(1.00)
    os.system("cls")
    time()


time()
