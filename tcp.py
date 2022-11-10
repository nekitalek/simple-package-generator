#TCP packet
from tkinter import Tk, ttk
from tkinter import *

class Example(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):

        self.lsource = Label(self, width=15, height=2, text="Source Port")
        self.esource = Entry(self, width=10)
        self.esource.insert(0, "20")
        self.ldest = Label(self, width=15, height=2, text="Denstination Port")
        self.edest = Entry(self, width=10)
        self.edest.insert(0, "80")
        self.SeqN = Label(self, width=20, height=1, text="Sequence Number               ")
        self.eSeqN = Entry(self, width=30)
        self.eSeqN.insert(0, "0")
        self.AckN = Label(self, width=20, height=1, text="Acknowledgment Number")
        self.eAckN = Entry(self, width=30)
        self.eAckN.insert(0, "0")
        self.Doff = Label(self, width=15, height=1, text="Data Offset")
        self.eDoff = Entry(self, width=5)
        self.flag = Label(self, width=15, height=2, text="Flags:   ")

        self.URGvar = IntVar()
        self.URGvar.set(0)
        self.URG = Checkbutton(self, text="URG", variable=self.URGvar, onvalue=32, offvalue=0)

        self.ACKvar = IntVar()
        self.ACKvar.set(0)
        self.ACK = Checkbutton(self, text="ACK", variable=self.ACKvar, onvalue=16, offvalue=0)

        self.PSHvar = IntVar()
        self.PSHvar.set(0)
        self.PSH = Checkbutton(self, text="PSH", variable=self.PSHvar, onvalue=8, offvalue=0)

        self.RSTvar = IntVar()
        self.RSTvar.set(0)
        self.RST = Checkbutton(self, text="RST", variable=self.RSTvar, onvalue=4, offvalue=0)

        self.SYNvar = IntVar()
        self.SYNvar.set(2)
        self.SYN = Checkbutton(self, text="SYN", variable=self.SYNvar, onvalue=2, offvalue=0)

        self.FINvar = IntVar()
        self.FINvar.set(0)
        self.FIN = Checkbutton(self, text="FIN ", variable=self.FINvar, onvalue=1, offvalue=0)

        self.ECNvar = IntVar()
        self.ECNvar.set(0)
        self.ECN = Checkbutton(self, text="ECN          ", variable=self.ECNvar, onvalue=256, offvalue=0)

        self.CWRvar = IntVar()
        self.CWRvar.set(0)
        self.CWR = Checkbutton(self, text="CWR         ", variable=self.CWRvar, onvalue=128, offvalue=0)

        self.echovar = IntVar()
        self.echovar.set(0)
        self.echo = Checkbutton(self, text="ECN-echo", variable=self.echovar, onvalue=64, offvalue=0)


        self.reser = Label(self, width=15, height=2, text="Reserved      ")
        self.ereser = Entry(self, width=10)
        self.ereser.insert(0, "0")
        self.Window = Label(self, width=10, height=2, text="Window")
        self.eWindow = Entry(self, width=10)
        self.eWindow.insert(0, "8192")
        self.Checksum= Label(self, width=10, height=1, text="Checksum       ")
        self.eChecksum = Entry(self, width=30)
        self.UrgP = Label(self, width=15, height=1, text="Urgent Pointer")
        self.eUrgP = Entry(self, width=30)
        self.eUrgP.insert(0, "0")
        self.Opt = Label(self, width=10, height=2, text=" Options")
        self.combobox = ttk.Combobox(self, width=10,values=["EOL", "NOP", "MSS"], height=3,state= "readonly")
        self.combobox.set("NOP")
        self.val = Label(self, width=5, height=2, text=" values")
        self.eval = Entry(self, width=10)

        self.lsource.grid(column=0, row=0)
        self.esource.grid(column=1, row=0)
        self.ldest.grid(column=2, row=0)
        self.edest.grid(column=3, row=0)
        self.SeqN.grid(column=0, row=1, columnspan=2)
        self.eSeqN.grid(column=2, row=1, columnspan=2)
        self.AckN.grid(column=0, row=2, columnspan=2)
        self.eAckN.grid(column=2, row=2, columnspan=2)
        self.Doff.grid(column=0,row=3)
        self.eDoff.grid(column=1, row=3)
        self.flag.grid(column=0, row=4)
        self.URG.grid(column=1, row=4)
        self.ACK.grid(column=1, row=5)
        self.PSH.grid(column=1, row=6)
        self.RST.grid(column=2, row=4)
        self.SYN.grid(column=2, row=5)
        self.FIN.grid(column=2, row=6)
        self.ECN.grid(column=3, row=4)
        self.CWR.grid(column=3, row=5)
        self.echo.grid(column=3, row=6)
        self.reser.grid(column=0, row=7)
        self.ereser.grid(column=1, row=7)
        self.Window.grid(column=2, row=7)
        self.eWindow.grid(column=3, row=7)
        self.Checksum.grid(column=0, row=8)
        self.eChecksum.grid(column=1, row=8, columnspan=2)
        self.UrgP.grid(column=0, row=10)
        self.eUrgP.grid(column=1, row=10, columnspan=2)
        self.Opt.grid(column=0, row=11)
        self.combobox.grid(column=1, row=11)
        self.val.grid(column=2, row=11)
        self.eval.grid(column=3, row=11)

        self.pack()
