#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python


from tkinter import *
from tkinter import messagebox


def calculate(*args):

  try:

    feet=feet_entry.get()
    if not feet:
       result_label["text"]=""
    else:
       metre=float(feet)*0.3048
       result_label["text"]=str(metre)

  except:

    messagebox.showerror("ERROR","Not a valid entry!")

window=Tk()
window.title("Feet to Metres")

window.rowconfigure([0,1,2],weight=1)
window.columnconfigure([0,1,2],weight=1)

feet_entry=Entry(master=window,width=8)
feet_entry.insert(0,"1")
feet_label=Label(master=window,text="feet")

equal_label=Label(master=window,text="is equivalent to")
result_label=Label(master=window,text="0.3048")
metre_label=Label(master=window,text="meters")

calculate_button=Button(master=window,text="Calculate",command=calculate)


feet_entry.grid(row=0,column=1,pady=10)
feet_entry.focus_set()
feet_label.grid(row=0,column=2,sticky="w",padx=10)

equal_label.grid(row=1,column=0)
result_label.grid(row=1,column=1)
metre_label.grid(row=1,column=2,sticky="w",padx=10)

calculate_button.grid(row=2,column=2,sticky="w",padx=10,pady=10)

window.bind("<Key>",calculate)

window.mainloop()
