from tkinter import *
from tkinter import ttk
import sys
import pytguess as pg

root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="Phasmophobot").grid(column=0, row=0)
ttk.Button(frm, text="Test2", command=pg.test2).grid(column=2, row=2)
ttk.Button(frm, text="Start Game Loop", command=pg.start).grid(column=3, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=10, row=2)
root.mainloop()