from tkinter import ttk
from tkinter import *
from tkinter import messagebox

from scapy.arch import get_if_hwaddr
from scapy.layers.inet import IP, UDP, TCP, ICMP, IPOption
import psutil
from scapy.layers.l2 import Ether
from scapy.sendrecv import srp, sr, sr1

import math


from ip import Example as TabA
from tcp import Example as TabB
from udp import Example as TabC
from icmp import Example as TabD

class MainWindow(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.notebook = ttk.Notebook(self, width=440, height=350)

        self.a_tab = TabA(self.notebook)
        self.b_tab = TabB(self.notebook)
        self.c_tab = TabC(self.notebook)
        self.d_tab = TabD(self.notebook)
        


        self.notebook.add(self.a_tab, text="IP")
        self.notebook.add(self.b_tab, text="TCP")
        self.notebook.add(self.c_tab, text="UDP")
        self.notebook.add(self.d_tab, text="ICMP")

        self.notebook.hide(self.b_tab)
        self.notebook.hide(self.c_tab)
        self.notebook.hide(self.d_tab)

        self.notebook.pack()

        self.pack()


class leftWindow(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.was = 0
        self.quantity_packages = 0
        self.l2 = Label(self, width=30, height=1, text="Protocols", bg="#FF4500")
        self.ip_ = Radiobutton(self, indicatoron=0, text="IP", variable=var, value=0, command=self.change, width=30, height=1, bg="#00BFFF")
        self.tcp_ = Radiobutton(self, indicatoron=0, text="TCP", variable=var, value=1, command=self.change, width=30, height=1, bg="#00BFFF")
        self.udp_ = Radiobutton(self, indicatoron=0, text="UDP", variable=var, value=2, command=self.change, width=30, height=1, bg="#00BFFF")
        self.ismp_ = Radiobutton(self, indicatoron=0, text="ICMP", variable=var, value=3, command=self.change, width=30, height=1, bg="#00BFFF")
        self.lsource = Label(self, width=31, height=1, text="Source IP", bg="#FFA500")
        self.esource = Entry(self, width=37)
        self.esource.insert(0, " "*25 + "192.168.100.5")
        self.lmacsource = Label(self, width=31, height=1, text="Source MAC address", bg="#FFA500")
        self.macsource = Entry(self, width=37)
        self.ldest = Label(self, width=31, height=1, text="Destination IP", bg="#FFA500")
        self.edest = Entry(self, width=37)
        self.edest.insert(0, " "*25 + "192.168.100.5")
        self.lmacdest = Label(self, width=31, height=1, text="Destination MAC address", bg="#FFA500")
        self.macdest = Entry(self, width=37)
        self.macdest.insert(0, " "*26 + "ff:ff:ff:ff:ff:ff")
        self.lne = Label(self, width=31, height=1, text="Network interface", bg="#FFA500")
        self.combobox = ttk.Combobox(self, values=key, height=4, width=33)
        self.combobox.set(key[4])
        self.combobox.bind("<<ComboboxSelected>>", self.ch)
        self.macsource.insert(0, " " * 23 + get_if_hwaddr(self.combobox.get()))
        self.bcre = Button(self, text="Create", height=1, width=30, command=self.creater, bg="#FFD700")
        self.bsen = Button(self, text="Send", height=1,width=30, command=self.sender, bg="#32CD32")

        self.l2.grid(column=0, row=0)
        self.ip_.grid(column=0, row=1)
        self.tcp_.grid(column=0, row=2)
        self.udp_.grid(column=0, row=3)
        self.ismp_.grid(column=0, row=4)
        self.lsource.grid(column=0, row=5)
        self.esource.grid(column=0, row=6)
        self.lmacsource.grid(column=0, row=7)
        self.macsource.grid(column=0, row=8)
        self.ldest.grid(column=0, row=9)
        self.edest.grid(column=0, row=10)
        self.lmacdest.grid(column=0, row=11)
        self.macdest.grid(column=0, row=12)
        self.lne.grid(column=0, row=13)
        self.combobox.grid(column=0, row=14)
        self.bcre.grid(column=0, row=15)
        self.bsen.grid(column=0, row=16)

        self.pack()

    def ch(self, event):
        self.macsource.delete(0, END)
        self.macsource.insert(0, " " * 23 + get_if_hwaddr(self.combobox.get()))

    def change(self):
        if (self.was != 0):
            ex.notebook.hide(self.was)

        if var.get() == 0:
            self.l2['text'] = 'IP protocol'
            self.was = 0
            ex.a_tab.comboprot.set("ip")
        elif var.get() == 1:
            self.l2['text'] = 'TCP protocol'
            ex.notebook.add(ex.b_tab, text="TCP")
            self.was = ex.b_tab
            ex.a_tab.comboprot.set("tcp")
        elif var.get() == 2:
            self.l2['text'] = 'UDP protocol'
            ex.notebook.add(ex.c_tab, text="UDP")
            self.was = ex.c_tab
            ex.a_tab.comboprot.set("udp")
        elif var.get() == 3:
            self.l2['text'] = 'ICMP protocol'
            ex.notebook.add(ex.d_tab, text="ICMP")
            self.was = ex.d_tab
            ex.a_tab.comboprot.set("icmp")

    def creater(self):
        src = self.esource.get().replace(" ", "")
        dst = self.edest.get().replace(" ", "")
        macsrc = self.macsource.get().replace(" ", "")
        macdst = self.macdest.get().replace(" ", "")
        lenI = self.Nons(ex.a_tab.enToL.get())
        ihl = self.Nons(ex.a_tab.enIHL.get())
        id = int(ex.a_tab.enIde.get())
        ttl = int(ex.a_tab.enTTL.get())
        chksum = self.Nons(ex.a_tab.enHChS.get())
        frag = int(ex.a_tab.enFOff.get())
        tos = int(ex.a_tab.enTOS.get())
        flags = ex.a_tab.cvar2.get() + ex.a_tab.cvar3.get() + ex.a_tab.cvar1.get()
        fcop = ex.a_tab.opt_var.get()
        proto = ex.a_tab.comboprot.get()
        options = [IPOption(copy_flag=int(ex.a_tab.opt_var.get()), optclass=int(ex.a_tab.rez_var.get()),
            option=ex.a_tab.combobox.get(), length=int(ex.a_tab.enleng.get()), value=ex.a_tab.envalu.get())]
        paylo = Re.get("1.0", END).replace("\n", "")

        print("IP: opt", ex.a_tab.combobox.get(), "/MACsrc", macsrc, "/MACdst", macdst, "/ihl", ihl, "/tos", tos, "/len", lenI, "/id", id, "/ttl", ttl, end=" ")
        print("/chksum", chksum, "/src", src, "/frag", frag, "/Flags: r M D", flags, "flags: copy", fcop, "proto", proto, "paylo", paylo, options)

        if var.get() == 0:
            self.packet = IP(src=src, dst=dst, id=id, len=lenI, ttl=ttl, chksum=chksum,
                                ihl=ihl, frag=frag, tos=tos, flags=flags, options=options, proto=proto)/paylo
            messagebox.showinfo('', 'Пакет IP создан')
        elif var.get() == 1:
            sport = int(ex.b_tab.esource.get())
            dport = int(ex.b_tab.edest.get())
            dataofs = self.Nons(ex.b_tab.eDoff.get())
            chksumT = self.Nons(ex.b_tab.eChecksum.get())
            urgptr = int(ex.b_tab.eUrgP.get())
            seq = int(ex.b_tab.eSeqN.get())
            ack = int(ex.b_tab.eAckN.get())
            reserved = int(ex.b_tab.ereser.get())
            window = int(ex.b_tab.eWindow.get())
            flagstcp = int(ex.b_tab.FINvar.get())+int(ex.b_tab.SYNvar.get())+int(ex.b_tab.RSTvar.get())
            flagstcp += int(ex.b_tab.PSHvar.get())+int(ex.b_tab.ACKvar.get())+int(ex.b_tab.URGvar.get())
            flagstcp += int(ex.b_tab.echovar.get()) + int(ex.b_tab.CWRvar.get()) + int(ex.b_tab.ECNvar.get())
            optionT = [(ex.b_tab.combobox.get(), ex.b_tab.eval.get())]
            print(ex.notebook.tab(ex.a_tab)['text']," / ",ex.notebook.tab(ex.b_tab)['text'])
            print("TCP IP: sport", sport, "/dport", dport, "/seq", seq, "ack", ack, "/dataofs", dataofs, "/chksum", chksum, end=" ")
            print("reserved", reserved, "urgptr", urgptr, "window", window, "flags", flagstcp, "optionT", optionT)

            self.packet = IP(src=src, dst=dst, id=id, len=lenI, ttl=ttl, chksum=chksum,
                                ihl=ihl, frag=frag, tos=tos, flags=flags, options=options, proto=proto)/\
                          TCP(sport=sport, dport=dport, seq=seq, ack=ack, dataofs=dataofs, chksum=chksumT,
                              urgptr=urgptr,reserved=reserved,window=window, flags=flagstcp,options=optionT)/paylo
            messagebox.showinfo('', 'Пакет TCP создан')
        elif var.get() == 2:
            sport = int(ex.c_tab.esource.get())
            dport = int(ex.c_tab.edest.get())
            lenU = self.Nons(ex.c_tab.eLeng.get())
            chksumU = self.Nons(ex.c_tab.eCheck.get())
            print(ex.notebook.tab(ex.a_tab)['text'], " / ", ex.notebook.tab(ex.c_tab)['text'])
            print("UDP: sport", sport, "/dport", dport, "/len", lenU, "/chksum", chksum)

            self.packet = IP(src=src, dst=dst, id=id, len=lenI, ttl=ttl,
                                chksum=chksum, ihl=ihl, frag=frag, tos=tos, flags=flags, proto=proto,
                                options=options)/UDP(sport=sport, dport=dport, len=lenU, chksum=chksumU)/paylo
            messagebox.showinfo('', 'Пакет UDP создан')
        elif var.get() == 3:
            type = int(ex.d_tab.typ_var.get())
            chksumIC = self.Nons(ex.d_tab.enHChS.get())
            code = int(ex.d_tab.ecode.get())
            seq = int(ex.d_tab.eSeqN.get())
            IdI = int(ex.d_tab.eID.get())
            print(ex.notebook.tab(ex.a_tab)['text'], " / ", ex.notebook.tab(ex.d_tab)['text'])
            print("ICMP: type", type)

            self.packet = IP(src=src, dst=dst, id=id, len=lenI, ttl=ttl,
                                chksum=chksum, ihl=ihl, frag=frag, tos=tos, flags=flags, proto=proto,
                                options=options)/ICMP(type=type, chksum=chksumIC, code=code, seq=seq, id=IdI)/paylo
            messagebox.showinfo('', 'Пакет ICMP создан')

        dequep.append(self.packet*int(count.get()))
        self.quantity_packages += int(count.get())
        deqcol.configure(text=self.quantity_packages)

    def Nons(self, atr):
        if (atr == ""):
            return None
        else:
            return int(atr)

    def sender(self):
        print("send", len(dequep), dequep)
        print("iface", self.combobox.get())
        for i in dequep:
            sr1(i, iface=self.combobox.get(), timeout=0.1)
        if self.quantity_packages == 0:
            messagebox.showinfo('', 'Нет сгенерированных пакетов')
        elif self.quantity_packages == 1:
            messagebox.showinfo('', 'Пакет отправлен')
        else:
            messagebox.showinfo('', "Пакеты отправлены")
        dequep.clear()
        self.quantity_packages = 0
        deqcol.configure(text=self.quantity_packages)

if __name__ == '__main__':

    root = Tk()
    root.title('Package Generator')
    addrs = psutil.net_if_addrs()
    key = list(addrs.keys())
    dequep = []
    print(key)
    var = IntVar()
    var.set(0)
    f1 = Frame(root)
    f2 = Frame(root)
    f3 = Frame(root)
    lab = Label(f3, width=10, height=1, text="Data")
    Re = Text(f3, width=15, height=12, font='Arial 14')
    deqL = Label(f3, width=20, height=1, text="Total number of packages")
    deqcol = Label(f3, width=5, text=0)
    coun = Label(f3, width=15, height=1, text="Count of packages ")
    count = Entry(f3, width=5)
    count.insert(0, 1)
    lab.pack()
    Re.pack()
    deqL.pack()
    deqcol.pack()
    coun.pack()
    count.pack()

    ex = MainWindow(f2)
    tex = leftWindow(f1)

    f1.grid(column=0, row=0)
    f2.grid(column=1, row=0)
    f3.grid(column=2, row=0)

    root.mainloop()