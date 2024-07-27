from tkinter import *
from tkinter.ttk import *
 
from time import strftime
 
tk = Tk()
tk.title('Clock')

def time():
    string = strftime('%A %D %H:%M:%S: %p')
    label.config(text=string)
    label.after(1000, time)
 
 
label = Label(tk, font=('Comic Sans MS', 40, 'bold'),
            background='black',
            foreground='green')
 
label.pack(anchor='s')
time()
 
mainloop()
