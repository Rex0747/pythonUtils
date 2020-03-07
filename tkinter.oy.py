
import tkinter
from tkinter import *
from tkinter import ttk
w = Tk()
w.geometry("640x700")

w.configure(bg = 'red')
w.title("mi TKINDER")

ttk.Button(w , text='EXIT' , command=quit).pack(side=BOTTOM)


w.mainloop()
