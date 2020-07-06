
#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python

from tkinter import *
import random

window=Tk()

def dice():

   number=str(random.randint(1,6))
   num_label["text"]=number


roll_button=Button(master=window,text="ROLL",command=dice)
num_label=Label(master=window)

roll_button.grid(row=0,column=0,sticky="nsew")
num_label.grid(row=1,column=0)

window.rowconfigure([0,1],weight=1,minsize=50)
window.columnconfigure(0,weight=1,minsize=150)


window.mainloop()
