#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python

from tkinter import *

window=Tk()

def tempconvert(*args):

    F_temp=float(F_entry.get())
    c_temp=(F_temp-32)*(5/9)
    c_label["text"]="{} {}".format(c_temp,"\N{DEGREE CELSIUS}")

entryFrame=Frame(master=window)


F_entry=Entry(master=entryFrame,width=10)
F_entry.insert(0,"32")
F_label=Label(master=entryFrame,text="\N{DEGREE FAHRENHEIT}")
F_entry.grid(row=0,column=0,pady=10,sticky="e")
F_label.grid(row=0,column=1,sticky="w")

arrowButton=Button(master=window,text="=",command=tempconvert)

c_label=Label(master=window,text="{} {}".format(0,"\N{DEGREE CELSIUS}"))

entryFrame.grid(row=0,column=0,padx=10)
arrowButton.grid(row=0,column=1,pady=10)
c_label.grid(row=0,column=3,padx=10)

entryFrame.rowconfigure(0,weight=1)
entryFrame.columnconfigure([0,1],weight=1)

window.rowconfigure(0,weight=1)
window.columnconfigure([0,1,2],weight=1)

F_entry.bind('<Return>',tempconvert)


window.mainloop()


