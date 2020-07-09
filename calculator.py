#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python

from tkinter import *

window=Tk()
window.title("Calculator")
window.resizable(False,False)

mainFrame=Frame(master=window)

screen_label=Label(master=mainFrame,height=3,bg="white",font="bold",
                   justify=LEFT,borderwidth=3,relief=RIDGE)

button0=Button(master=mainFrame,text="0",bg="white",width=4,height=3)
button1=Button(master=mainFrame,text="1",bg="white",width=4,height=3)
button2=Button(master=mainFrame,text="2",bg="white",width=4,height=3)
button3=Button(master=mainFrame,text="3",width=4,bg="white",height=3)
button4=Button(master=mainFrame,text="4",width=4,height=3,bg="white")
button5=Button(master=mainFrame,text="5",width=4,height=3,bg="white")
button6=Button(master=mainFrame,text="6",width=4,height=3,bg="white")
button7=Button(master=mainFrame,text="7",width=4,height=3,bg="white")
button8=Button(master=mainFrame,text="8",width=4,height=3,bg="white")
button9=Button(master=mainFrame,text="9",width=4,height=3,bg="white")

buttonADD=Button(master=mainFrame,text="+",width=4,height=3,bg="white")
buttonSUB=Button(master=mainFrame,text="-",width=4,height=3,bg="white")
buttonMUL=Button(master=mainFrame,text="X",width=4,height=3,bg="white")
buttonDIV=Button(master=mainFrame,text="/",width=4,height=3,bg="white")

buttonCLEAR=Button(master=mainFrame,text="C",width=4,height=3,bg="white")
buttonEQUAL=Button(master=mainFrame,text="=",width=4,height=3,bg="white")
buttonX=Button(master=mainFrame,text="1/x",width=4,height=3,bg="white")
buttonSQRT=Button(master=mainFrame,text="√",width=4,height=3,bg="white")


button7.grid(row=1,column=0,padx=3,pady=3,sticky="nsew")
button8.grid(row=1,column=1,padx=3,pady=3,sticky="nsew")
button9.grid(row=1,column=2,padx=3,pady=3,sticky="nsew")
button4.grid(row=2,column=0,padx=3,pady=3,sticky="nsew")
button5.grid(row=2,column=1,padx=3,pady=3,sticky="nsew")
button6.grid(row=2,column=2,padx=3,pady=3,sticky="nsew")
button1.grid(row=3,column=0,padx=3,pady=3,sticky="nsew")
button2.grid(row=3,column=1,padx=3,pady=3,sticky="nsew")
button3.grid(row=3,column=2,padx=3,pady=3,sticky="nsew")
button0.grid(row=4,column=0,columnspan=2,padx=3,pady=3,sticky="nsew")

buttonCLEAR.grid(row=4,column=2,padx=3,pady=3,sticky="nsew")
buttonEQUAL.grid(row=3,column=4,rowspan=2,padx=3,pady=3,sticky="nsew")
buttonSQRT.grid(row=1,column=4,padx=3,pady=3,sticky="nsew")
buttonX.grid(row=2,column=4,padx=3,pady=3,sticky="nsew")

buttonADD.grid(row=4,column=3,padx=3,pady=3,sticky="nsew")
buttonSUB.grid(row=3,column=3,padx=3,pady=3,sticky="nsew")
buttonMUL.grid(row=2,column=3,padx=3,pady=3,sticky="nsew")
buttonDIV.grid(row=1,column=3,padx=3,pady=3,sticky="nsew")


mainFrame.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
screen_label.grid(row=0,column=0,columnspan=5,pady=10,sticky="nsew")

window.mainloop()
