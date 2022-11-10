#icmp packet
from tkinter import *

class Example(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
       self.typ_var = IntVar()
       self.typ_var.set(8)
       self.typ = Label(self, width=10, height=2, text="Type")
       self.typ1 = Radiobutton(self, text='Echo request', variable=self.typ_var, value=8, height=1)
       self.typ2 = Radiobutton(self, text='Echo reply    ', variable=self.typ_var, value=0, height=1)

       self.code = Label(self, width=10, height=2, text="Code")
       self.ecode = Entry(self, width=10)
       self.ecode.insert(0, "0")
       self.ID = Label(self, width=10, height=2, text="Id")
       self.eID = Entry(self, width=10)
       self.eID.insert(0, "0")
       self.HChS = Label(self, width=15, height=2, text="Header  Checksum")
       self.enHChS = Entry(self, width=25)
       self.SeqN = Label(self, width=15, height=2, text="Sequence Number")
       self.eSeqN = Entry(self, width=25)
       self.eSeqN.insert(0, "0")

       self.typ.grid(column=0, row=0)
       self.typ1.grid(column=1, row=0)
       self.typ2.grid(column=2, row=0)
       self.code.grid(column=0, row=1)
       self.ecode.grid(column=1, row=1)
       self.ID.grid(column=2, row=1)
       self.eID.grid(column=3, row=1)
       self.HChS.grid(column=0, row=3, columnspan=2)
       self.enHChS.grid(column=2, row=3, columnspan=2)
       self.SeqN.grid(column=0, row=4, columnspan=2)
       self.eSeqN.grid(column=2, row=4, columnspan=2)

       self.pack()

