#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python

from tkinter import *
import time

window=Tk()
window.geometry("800x170")

def clock():

    hour=time.strftime("%H")
    minute=time.strftime("%M")
    second=time.strftime("%S")

    display="{} : {} : {}".format(hour,minute,second)
    clockLabel.config(text=display)
    clockLabel.after(1000,clock)

clockLabel=Label(master=window,text="",font=("Timer",110),fg="red",bg="black")
clockLabel.pack(fill="both")

clock()

window.mainloop()
