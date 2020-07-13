#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python

from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox

window=Tk()
window.title("User Data Storage Form")
window.resizable(False,False)


#connection=sqlite3.connect("UserData.db")
#db_cursor=connection.cursor()

#db_cursor.execute(""CREATE TABLE
#data(firstname text,
#    lastname text,
#     address text,
#     district text,
#     state text,
#     pincode text
#    )
#""")

#connection.commit()
#connection.close()


def submit():

    connection=sqlite3.connect("UserData.db")
    db_cursor=connection.cursor()


    db_cursor.execute("INSERT INTO data VALUES (:f_name,:l_name,:address,:district,:state,:pin ) ",
                      {
                       'f_name':fnameEntry.get(),
                       'l_name':lnameEntry.get(),
                       'address':addressEntry.get(),
                       'district':districtEntry.get(),
                       'state':stateEntry.get(),
                       'pin':pinEntry.get()
                      })


    connection.commit()
    connection.close()

    fnameEntry.delete(0,END)
    lnameEntry.delete(0,END)
    addressEntry.delete(0,END)
    districtEntry.delete(0,END)
    stateEntry.delete(0,END)
    pinEntry.delete(0,END)

    messagebox.showinfo("SUCCESS","Data was submitted succesfully!")

def check(condition):

    global passwordEntry
    global usernameEntry
    global entryFrame
    global checkFrame
    global recordWindow

    recordWindow=Toplevel(master=window)
    recordWindow.title("authentication")
    recordWindow.resizable(False,False)

    entryFrame=Frame(master=recordWindow,bd=3)

    usernamelabel=Label(master=entryFrame,text="Username:")
    usernamelabel.grid(row=0,column=0,sticky="e")
    passwordlabel=Label(master=entryFrame,text="Password:")
    passwordlabel.grid(row=1,column=0,sticky="e")

    usernameEntry=Entry(master=entryFrame,width=30)
    usernameEntry.grid(row=0,column=1,sticky="w",pady=5)
    passwordEntry=Entry(master=entryFrame,width=30)
    passwordEntry.grid(row=1,column=1,sticky="w",pady=5)

    passwordEntry.config(show="*")

    entryFrame.grid(row=0,column=0,sticky="nsew")

    checkFrame=Frame(master=recordWindow)

    checkButton=Button(master=checkFrame,text="Submit",width=7,command=condition)
    checkButton.grid(row=0,column=1,pady=5,padx=5,sticky="ew")

    checkFrame.grid(row=1,column=0,sticky="e")


def show():

    if passwordEntry.get()=="raspberry" and usernameEntry.get() == "pi":

       display=Toplevel(master=window)
       display.title("User Data")

       connection=sqlite3.connect("UserData.db")
       db_cursor=connection.cursor()


       db_cursor.execute("SELECT *,oid FROM data")
       records=db_cursor.fetchall()

       connection.commit()
       connection.close()

       for index,record in enumerate(records):

         fname,lname,address,district,state,pin,oid=record

         recordWindow.destroy()

         displayFrame=Frame(master=display,bd=10,relief=RIDGE)

         nameLabel=Label(master=displayFrame,text="Name:")
         nameLabel.grid(row=0,column=0,sticky="e",pady=(5,0))
         addressLabel=Label(master=displayFrame,text="Address:")
         addressLabel.grid(row=1,column=0,sticky="e",pady=(5,0))
         districtLabel=Label(master=displayFrame,text="District:")
         districtLabel.grid(row=2,column=0,sticky="e",pady=(5,0))
         stateLabel=Label(master=displayFrame,text="State:")
         stateLabel.grid(row=3,column=0,sticky="e",pady=(5,0))
         pinLabel=Label(master=displayFrame,text="Pincode:")
         pinLabel.grid(row=4,column=0,sticky="e",pady=(5,5))
         idLabel=Label(master=displayFrame,text="ID:")
         idLabel.grid(row=5,column=0,sticky="e",pady=(5,5))


         namelabel=Label(master=displayFrame,text="{} {}".format(fname,lname))
         namelabel.grid(row=0,column=1,sticky="w",pady=(5,0))
         addresslabel=Label(master=displayFrame,text=address)
         addresslabel.grid(row=1,column=1,sticky="w",pady=(5,0))
         districtlabel=Label(master=displayFrame,text=district)
         districtlabel.grid(row=2,column=1,sticky="w",pady=(5,0))
         statelabel=Label(master=displayFrame,text=state)
         statelabel.grid(row=3,column=1,sticky="w",pady=(5,0))
         pinlabel=Label(master=displayFrame,text=pin)
         pinlabel.grid(row=4,column=1,sticky="w",pady=(5,5))
         idLabel=Label(master=displayFrame,text=oid)
         idLabel.grid(row=5,column=1,sticky="w",pady=(5,5))

         displayFrame.pack(fill=BOTH)

    else:

       messagebox.showerror("AUTHENTICATION ERROR","Invalid Credentials")


def get_id():

    global deleteEntry
    global deleteDisplay

    if passwordEntry.get()=="raspberry" and usernameEntry.get() == "pi":

       deleteDisplay=Toplevel(master=window)
       deleteDisplay.title("Delete User Data")

       recordWindow.destroy()

       deleteDisplayFrame=Frame(master=deleteDisplay,bd=3,relief=SUNKEN)

       deleteLabel=Label(master=deleteDisplayFrame,text="Enter ID to be deleted:")
       deleteLabel.grid(row=0,column=0,sticky="e",pady=(5,0))

       deleteEntry=Entry(master=deleteDisplayFrame,width=10)
       deleteEntry.grid(row=0,column=1,sticky="w",pady=(5,0))

       deleteDisplayFrame.grid(row=0,column=0,sticky="nsew")

       deleteFrame=Frame(master=deleteDisplay)

       deleteButton=Button(master=deleteFrame,text="Delete",width=7,command=delete)
       deleteButton.grid(row=0,column=1,pady=5,padx=5,sticky="ew")

       deleteFrame.grid(row=1,column=0,sticky="e")

    else:

       messagebox.showerror("AUTHENTICATION ERROR","Invalid Credentials")


def delete():

    global delete_id
    delete_id=deleteEntry.get()

    connection=sqlite3.connect("UserData.db")
    db_cursor=connection.cursor()

    db_cursor.execute("DELETE FROM data WHERE oid ="+deleteEntry.get())


    connection.commit()
    connection.close()

    deleteDisplay.destroy()

    messagebox.showinfo("SUCCESS","ID number was {} deleted successfully!".format(delete_id))

def get_data():

    global editDisplay
    global editEntry


    if passwordEntry.get()=="raspberry" and usernameEntry.get() == "pi":

       editDisplay=Toplevel(master=window)
       editDisplay.title("Edit User Data")

       recordWindow.destroy()

       editDisplayFrame=Frame(master=editDisplay,bd=3,relief=SUNKEN)

       editLabel=Label(master=editDisplayFrame,text="Enter ID to be edited:")
       editLabel.grid(row=0,column=0,sticky="e",pady=(5,0))

       editEntry=Entry(master=editDisplayFrame,width=10)
       editEntry.grid(row=0,column=1,sticky="w",pady=(5,0))

       editDisplayFrame.grid(row=0,column=0,sticky="nsew")

       editFrame=Frame(master=editDisplay)

       editButton=Button(master=editFrame,text="Edit",width=7,command=edit)
       editButton.grid(row=0,column=1,pady=5,padx=5,sticky="ew")

       editFrame.grid(row=1,column=0,sticky="e")

    else:

       messagebox.showerror("AUTHENTICATION ERROR","Invalid Credentials")


def edit():

       global data_id
       global edit_fnameEntry
       global edit_lnameEntry
       global edit_addressEntry
       global edit_districtEntry
       global edit_stateEntry
       global edit_pinEntry
       global editwindow

       data_id=editEntry.get()

       editwindow=Toplevel(master=window)
       editwindow.title("Edit User Data")

       editFrame=Frame(master=editwindow,bd=3,relief="sunken")

       edit_fnameLabel=Label(master=editFrame,text="First Name:")
       edit_fnameLabel.grid(row=0,column=0,sticky="e",pady=(5,0))
       edit_lnameLabel=Label(master=editFrame,text="Last Name:")
       edit_lnameLabel.grid(row=1,column=0,sticky="e",pady=(5,0))
       edit_addressLabel=Label(master=editFrame,text="Address:")
       edit_addressLabel.grid(row=2,column=0,sticky="e",pady=(5,0))
       edit_districtLabel=Label(master=editFrame,text="District:")
       edit_districtLabel.grid(row=3,column=0,sticky="e",pady=(5,0))
       edit_stateLabel=Label(master=editFrame,text="State/Province:")
       edit_stateLabel.grid(row=4,column=0,sticky="e",pady=(5,0))
       edit_pinLabel=Label(master=editFrame,text="Pin Code:")
       edit_pinLabel.grid(row=5,column=0,sticky="e",pady=(5,0))

       edit_fnameEntry=Entry(master=editFrame,width=50)
       edit_fnameEntry.grid(row=0,column=1,sticky="w",pady=(5,0))
       edit_lnameEntry=Entry(master=editFrame,width=50)
       edit_lnameEntry.grid(row=1,column=1,sticky="w",pady=(5,0))
       edit_addressEntry=Entry(master=editFrame,width=50)
       edit_addressEntry.grid(row=2,column=1,sticky="w",pady=(5,0))
       edit_districtEntry=Entry(master=editFrame,width=50)
       edit_districtEntry.grid(row=3,column=1,sticky="w",pady=(5,0))
       edit_stateEntry=Entry(master=editFrame,width=50)
       edit_stateEntry.grid(row=4,column=1,sticky="w",pady=(5,0))
       edit_pinEntry=Entry(master=editFrame,width=50)
       edit_pinEntry.grid(row=5,column=1,sticky="w",pady=(5,5))

       editFrame.grid(row=0,column=0,sticky="nsew")

       edit_buttonFrame=Frame(master=editwindow)

       editButton=Button(master=edit_buttonFrame,text="Ok",width=7,command=upload)
       editButton.grid(row=0,column=3,pady=5,padx=5,sticky="ew")

       edit_buttonFrame.grid(row=1,column=0,sticky="e")


       connection=sqlite3.connect("UserData.db")
       db_cursor=connection.cursor()

       db_cursor.execute("SELECT * FROM data WHERE oid ="+editEntry.get())

       records=db_cursor.fetchall()

       for record in records:

           edit_fnameEntry.insert(0,record[0])
           edit_lnameEntry.insert(0,record[1])
           edit_addressEntry.insert(0,record[2])
           edit_districtEntry.insert(0,record[3])
           edit_stateEntry.insert(0,record[4])
           edit_pinEntry.insert(0,record[5])

       connection.commit()
       connection.close()

       editDisplay.destroy()

def upload():

    connection=sqlite3.connect("UserData.db")
    db_cursor=connection.cursor()

    db_cursor.execute(""" UPDATE data SET
                      firstname = :fname,
                      lastname = :lname,
                      address = :address,
                      district = :district,
                      state = :state,
                      pincode = :pin
                      WHERE oid = :oid""",
                      {

                       'fname':edit_fnameEntry.get(),
                       'lname':edit_lnameEntry.get(),
                       'address':edit_addressEntry.get(),
                       'district':edit_districtEntry.get(),
                       'state':edit_stateEntry.get(),
                       'pin':edit_pinEntry.get(),
                       'oid':data_id
                        })

    connection.commit()
    connection.close()

    editwindow.destroy()

    messagebox.showinfo("SUCCESS","ID Number {} was edited successfully!".format(data_id))



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

submitButton=Button(master=buttonFrame,text="Submit",width=7,command=submit)
submitButton.grid(row=0,column=3,pady=5,padx=5,sticky="ew")
editButton=Button(master=buttonFrame,text="Edit",width=7,command=lambda:check(get_data))
editButton.grid(row=0,column=2,pady=5,padx=5,sticky="ew")
deleteButton=Button(master=buttonFrame,text="Delete",width=7,command=lambda:check(get_id))
deleteButton.grid(row=0,column=1,pady=5,padx=5,sticky="ew")
showButton=Button(master=buttonFrame,text="Show",width=7,command=lambda:check(show))
showButton.grid(row=0,column=0,pady=5,padx=5,sticky="ew")

buttonFrame.grid(row=1,column=0,sticky="e")

window.mainloop()
