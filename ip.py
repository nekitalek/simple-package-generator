#IP packet

from tkinter import *
from tkinter import Tk, ttk
class Example(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.r_var = BooleanVar()
        self.r_var.set(0)
        self.vers=Label(self, width=10, height=1, text="IP verson")
        self.r1 = Radiobutton(self,text='IPv4', variable=self.r_var, value=0, height=1)
        self.r2 = Radiobutton(self,text='IPv6', variable=self.r_var, value=1, height=1)
        self.IHL = Label(self, width=5, height=1, text="IHL")
        self.enIHL = Entry(self, width=8)
        self.TOS = Label(self, width=5, height=1, text="TOS")
        self.enTOS = Entry(self, width=8)
        self.enTOS.insert(0, "0")
        self.ToL = Label(self, width=15, height=1, text="Total Length       ")
        self.enToL = Entry(self, width=10)
        self.Ide = Label(self, width=15, height=1, text="Identification     ")
        self.enIde = Entry(self, width=10)
        self.enIde.insert(0, "1")

        self.Fl = Label(self, width=10, height=1, text="Flags   ")
        self.cvar1 = IntVar()
        self.cvar1.set(0)
        self.fl1 = Checkbutton(self, text="Reserved", variable=self.cvar1, onvalue=4, offvalue=0)

        self.cvar2 = IntVar()
        self.cvar2.set(0)
        self.fl2 = Checkbutton(self, text="MF   ", variable=self.cvar2, onvalue=1, offvalue=0)

        self.cvar3 = IntVar()
        self.cvar3.set(0)
        self.fl3 = Checkbutton(self, text="DF        ", variable=self.cvar3, onvalue=2, offvalue=0)

        self.FOff = Label(self, width=15, height=1, text="Fragment Offset")
        self.enFOff = Entry(self, width=10)
        self.enFOff.insert(0, "0")

        self.TTL = Label(self, width=5, height=1, text="TTL")
        self.enTTL = Entry(self, width=8)
        self.enTTL.insert(0, "64")

        self.HChS = Label(self, width=15, height=1, text="  Header  Checksum")
        self.enHChS = Entry(self, width=25)

        self.Opt = Label(self, width=10, height=1, text="Options:")
        self.Flc = Label(self, width=5, height=1, text="flags")

        self.opt_var = IntVar()
        self.opt_var.set(0)

        self.fcp1 = Radiobutton(self, text='No copy', variable=self.opt_var, value=0, height=1)
        self.fcp2 = Radiobutton(self, text='Copy     ', variable=self.opt_var, value=1, height=1)

        self.rez_var = IntVar()
        self.rez_var.set(0)
        print(self.rez_var.set)

        self.Rez = Label(self, width=5, height=1, text="mode")
        self.rez1 = Radiobutton(self, text='Debug  ', variable=self.rez_var, value=2, height=1)
        self.rez2 = Radiobutton(self, text='Control ', variable=self.rez_var, value=0, height=1)
        self.var = StringVar()
        self.value=["end_of_list", "nop", "security", "loose_source_route", "timestamp", "extended_security",
"commercial_security", "record_route", "stream_id", "strict_source_route","experimental_measurement", "mtu_probe", "mtu_reply", "flow_control", "access_control", "encode",
"imi_traffic_descriptor", "extended_IP", "traceroute", "address_extension", "router_alert",
"selective_directed_broadcast_mode", "dynamic_packet_state", "upstream_multicast_packet",
"quick_start", "rfc4727_experiment"]
        self.combobox = ttk.Combobox(self, width=18, values=self.value, height=4, state="readonly", textvariable=self.var)
        self.combobox.set("nop")
        self.Lprot = Label(self, width=8, height=1, text="protocol")
        self.varp = StringVar()
        self.comboprot = ttk.Combobox(self, width=8, values=["ip", "tcp", "udp", "icmp"], height=4, state="readonly",
                                     textvariable=self.varp)
        self.comboprot.set("ip")

        self.val = Label(self, width=10, height=1, text="option")
        self.leng = Label(self, width=10, height=1, text="Length")
        self.enleng = Entry(self, width=10)
        self.enleng.insert(0, "0")
        self.valu = Label(self, width=10, height=1, text="Value ")
        self.envalu = Entry(self, width=10)
        self.enleng["state"] = DISABLED
        self.envalu["state"] = DISABLED

        self.vers.grid(column=0, row=0)
        self.r1.grid(column=0, row=1)
        self.r2.grid(column=0, row=2)
        self.IHL.grid(column=1, row=0)
        self.enIHL.grid(column=2, row=0)
        self.TOS.grid(column=1, row=1)
        self.enTOS.grid(column=2, row=1)
        self.ToL.grid(column=3, row=2, columnspan=2)
        self.enToL.grid(column=5, row=2)
        self.Ide.grid(column=3, row=0, columnspan=2)
        self.enIde.grid(column=5, row=0)
        self.Fl.grid(column=0, row=3)
        self.fl1.grid(column=1, row=3)
        self.fl2.grid(column=2, row=3)
        self.fl3.grid(column=3, row=3)
        self.FOff.grid(column=3, row=1,columnspan=2)
        self.enFOff.grid(column=5, row=1)
        self.TTL.grid(column=1, row=2)
        self.enTTL.grid(column=2, row=2)
        self.HChS.grid(column=0, row=4,columnspan=2)
        self.enHChS.grid(column=2, row=4,columnspan=3)
        self.Opt.grid(column=0, row=5)
        self.Flc.grid(column=0, row=6)
        self.fcp1.grid(column=0, row=7)
        self.fcp2.grid(column=0, row=8)
        self.Rez.grid(column=1, row=6)
        self.rez1.grid(column=1, row=7)
        self.rez2.grid(column=1, row=8)
        self.combobox.grid(column=2, row=7,columnspan=2)
        self.val.grid(column=2, row=6)
        self.leng.grid(column=4, row=7)
        self.enleng.grid(column=5, row=7)
        self.valu.grid(column=4, row=8)
        self.envalu.grid(column=5, row=8)
        self.Lprot.grid(column=0, row=9)
        self.comboprot.grid(column=1, row=9)

        self.combobox.bind('<<ComboboxSelected>>', self.blocks)
        self.pack()


    def blocks(self,event):
        s = self.var.get()
        if (s == "end_of_list" or s == "nop"):
            self.enleng["state"] = DISABLED
            self.envalu["state"] = DISABLED
        else:
            self.enleng["state"] = NORMAL
            self.envalu["state"] = NORMAL

