#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python

from tkinter import *
from PIL import ImageTk,Image
import sqlite3


window=Tk()
window.title=("User Data Storage Form")



mainFrame=Frame(master=window,bd=3,relief="sunken")

fnameLabel=Label(master=mainFrame,text="First Name:")
fnameLabel.grid(row=0,column=0,sticky="e",pady=(5,0))
lnameLabel=Label(master=mainFrame,text="Last Name:")
lnameLabel.grid(row=1,column=0,sticky="e",pady=(5,0))
addressLabel=Label(master=mainFrame,text="Address:")
addressLabel.grid(row=2,column=0,sticky="e",pady=(5,0))
districtLabel=Label(master=mainFrame,text="District:")
districtLabel.grid(row=3,column=0,sticky="e",pady=(5,0))
stateLabel=Label(master=mainFrame,text="State/Province:")
stateLabel.grid(row=4,column=0,sticky="e",pady=(5,0))
pinLabel=Label(master=mainFrame,text="Pin Code:")
pinLabel.grid(row=5,column=0,sticky="e",pady=(5,0))


fnameEntry=Entry(master=mainFrame,width=50)
fnameEntry.grid(row=0,column=1,sticky="w",pady=(5,0))
lnameEntry=Entry(master=mainFrame,width=50)
lnameEntry.grid(row=1,column=1,sticky="w",pady=(5,0))
addressEntry=Entry(master=mainFrame,width=50)
addressEntry.grid(row=2,column=1,sticky="w",pady=(5,0))
districtEntry=Entry(master=mainFrame,width=50)
districtEntry.grid(row=3,column=1,sticky="w",pady=(5,0))
stateEntry=Entry(master=mainFrame,width=50)
stateEntry.grid(row=4,column=1,sticky="w",pady=(5,0))
pinEntry=Entry(master=mainFrame,width=50)
pinEntry.grid(row=5,column=1,sticky="w",pady=(5,5))

mainFrame.grid(row=0,column=0,sticky="nsew")

buttonFrame=Frame(master=window)

submitButton=Button(master=buttonFrame,text="Submit",width=7)
submitButton.grid(row=0,column=3,pady=5,padx=5,sticky="ew")

editButton=Button(master=buttonFrame,text="Edit",width=7)
editButton.grid(row=0,column=2,pady=5,padx=5,sticky="ew")

deleteButton=Button(master=buttonFrame,text="Delete",width=7)
deleteButton.grid(row=0,column=1,pady=5,padx=5,sticky="ew")

showButton=Button(master=buttonFrame,text="Show",width=7)
showButton.grid(row=0,column=0,pady=5,padx=5,sticky="ew")

buttonFrame.grid(row=1,column=0,sticky="e")

window.mainloop()
