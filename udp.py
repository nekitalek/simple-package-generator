#UDP packet
from tkinter import *
class Example(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
       self.lsource = Label(self, width=15, height=2, text="Source Port")
       self.esource = Entry(self, width=15)
       self.esource.insert(0, "53")
       self.ldest = Label(self, width=15, height=2, text="Denstination Port")
       self.edest = Entry(self, width=15)
       self.edest.insert(0, "53")
       self.Leng = Label(self, width=15, height=2, text="Length")
       self.eLeng = Entry(self, width=15)
       self.Check = Label(self, width=15, height=2, text="Checksum")
       self.eCheck = Entry(self, width=15)

       self.lsource.grid(column=0, row=0)
       self.esource.grid(column=1, row=0)
       self.ldest.grid(column=2, row=0)
       self.edest.grid(column=3, row=0)
       self.Leng.grid(column=0, row=1)
       self.eLeng.grid(column=1, row=1)
       self.Check.grid(column=2, row=1)
       self.eCheck.grid(column=3, row=1)

       self.pack()
