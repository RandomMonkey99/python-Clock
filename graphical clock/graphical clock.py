#-------Please follow me-------

from tkinter import *
from tkinter.ttk import *
 
from time import strftime
 
tk = Tk()
tk.title('Clock')

def time():
    string = strftime('%A %D %H:%M:%S: %p')
    label.config(text=string)
    label.after(1000, time)
 
 
label = Label(tk, font=('Comic Sans MS', 40, 'bold'), #you can change the font (https://github.com/RandomMonkey99/python-Clock/blob/main/disponible%20tkinter%20fonts.md) the text size and the stile(bold, italic, underline)
            background='black',#you can change background and foreground
            foreground='green')
 
label.pack(anchor='s')
time()
 
tk.mainloop()
