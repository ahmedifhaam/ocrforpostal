#!/usr/bin/python

from tkinter import *
# from _tkinter import *
# from Tkinter import *
import tkinter.messagebox as tkmsgbox

# import tkinter.tkMessageBox as tkmsgbox
# from tkMessageBox import *
#

top = Tk()

frame1 = Frame(top)
frame1.pack(fill=X)

L1 = Label(frame1,text="Line one")
L1.pack(side=LEFT)
E1 = Entry(frame1,bd=5)
E1.pack(side=RIGHT)

frame2 = Frame(top)
frame2.pack(fill=X)

L2 = Label(frame2,text="line two")
L2.pack(side=LEFT)
E2 = Entry(frame2,bd=5)
E2.pack(side=RIGHT)

frame3 = Frame(top)
frame3.pack(fill=X)

L3 = Label(frame3,text="Line three")
L3.pack(side=LEFT)
E3 = Entry(frame3,bd=5)
E3.pack(side=RIGHT)

def printText():
	tkmsgbox.showinfo("Hi","Line 1 : "+E1.get()+"\nLine 2 : "+E2.get()+"\nLine 3"+E3.get())
	top.quit()


okbtn = Button(text=u'\u0D85',command=printText)

strVar = StringVar()

btnA = Button(text='cancel',command=printText)

btnA.pack()
okbtn.pack()
top.mainloop()
