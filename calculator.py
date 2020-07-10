#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python

from tkinter import *

operation=None
check=True
def number(num):

    global check
    if check:
       screen_label["text"]=""
       check=False
    screen_label["text"]=screen_label["text"]+str(num)

def add():
    global operation
    if not screen_label["text"]:
       operaion="add"
       return
    global first_num
    if operation=="add":
       sec_num=float(screen_label["text"])
       first_num=first_num+sec_num
       screen_label["text"]=""
    elif operation=="sub":
       sec_num=float(screen_label["text"])
       first_num=first_num-sec_num
       screen_label["text"]=""
    elif operation=="mul":
       sec_num=float(screen_label["text"])
       first_num=first_num*sec_num
       screen_label["text"]=""
    elif operation=="div":
       if float(screen_label["text"])==0:
          clear()
          return
       sec_num=float(screen_label["text"])
       first_num=first_num/sec_num
       screen_label["text"]=""
    else:
       first_num=float(screen_label["text"])
       screen_label["text"]=""
    operation="add"

def subtract():

    global operation
    if not screen_label["text"]:
       operation="sub"
       return
    global first_num
    if operation=="add":
       sec_num=float(screen_label["text"])
       first_num=first_num+sec_num
       screen_label["text"]=""
    elif operation=="sub":
       sec_num=float(screen_label["text"])
       first_num=first_num-sec_num
       screen_label["text"]=""
    elif operation=="mul":
       sec_num=float(screen_label["text"])
       first_num=first_num*sec_num
       screen_label["text"]=""
    elif operation=="div":
       if float(screen_label["text"])==0:
          clear()
          return
       sec_num=float(screen_label["text"])
       first_num=first_num/sec_num
       screen_label["text"]=""
    else:
       first_num=float(screen_label["text"])
       screen_label["text"]=""
    operation="sub"

def multiply():

    global operation
    if not screen_label["text"]:
       operation="mul"
       return
    global first_num
    if operation=="add":
       sec_num=float(screen_label["text"])
       first_num=first_num+sec_num
       screen_label["text"]=""
    elif operation=="sub":
       sec_num=float(screen_label["text"])
       first_num=first_num-sec_num
       screen_label["text"]=""
    elif operation=="mul":
       sec_num=float(screen_label["text"])
       first_num=first_num*sec_num
       screen_label["text"]=""
    elif operation=="div":
       if float(screen_label["text"])==0:
          clear()
          return
       sec_num=float(screen_label["text"])
       first_num=first_num/sec_num
       screen_label["text"]=""
    else:
       first_num=float(screen_label["text"])
       screen_label["text"]=""
    operation="mul"

def divide():

    global operation
    if not screen_label["text"]:
       operation="div"
       return
    global first_num
    if operation=="add":
       sec_num=float(screen_label["text"])
       first_num=first_num+sec_num
       screen_label["text"]=""
    elif operation=="sub":
       sec_num=float(screen_label["text"])
       first_num=first_num-sec_num
       screen_label["text"]=""
    elif operation=="mul":
       sec_num=float(screen_label["text"])
       first_num=first_num*sec_num
       screen_label["text"]=""
    elif operation=="div":
       if float(screen_label["text"])==0:
          clear()
          return
       sec_num=float(screen_label["text"])
       first_num=first_num/sec_num
       screen_label["text"]=""
    else:
       first_num=float(screen_label["text"])
       screen_label["text"]=""
    operation="div"

def clear():

    global operation
    global first_num
    screen_label["text"]=""
    operation=None
    first_num=None

def equal():

    global first_num
    global operation
    global check
    if not screen_label["text"]:
       screen_label["text"]=str(first_num)
       first_num=None
       operation=None
       check=True
       return
    if operation=="add":
       sec_num=float(screen_label["text"])
       first_num=first_num+sec_num
       screen_label["text"]=""
    elif operation=="sub":
       sec_num=float(screen_label["text"])
       first_num=first_num-sec_num
       screen_label["text"]=""
    elif operation=="mul":
       sec_num=float(screen_label["text"])
       first_num=first_num*sec_num
       screen_label["text"]=""
    elif operation=="div":
       if float(screen_label["text"])==0:
          clear()
          return
       sec_num=float(screen_label["text"])
       first_num=first_num/sec_num
       screen_label["text"]=""
    else:
       return

    screen_label["text"]=str(first_num)
    operation=None
    check=True

def sqrt():
    global first_num
    global operation
    if not screen_label["text"]:
       return
    screen_label["text"]=str(float(screen_label["text"])**0.5)
    first_num=screen_label["text"]
    operation=None

def reciprocal():

    global first_num
    global operation
    if not screen_label["text"] or float(screen_label["text"])==0:
       return
    screen_label["text"]=str(1/(float(screen_label["text"])))
    first_num=screen_label["text"]
    operation=None


window=Tk()
window.title("Calculator")
window.resizable(False,False)
mainFrame=Frame(master=window)

screen_label=Label(master=mainFrame,height=3,bg="white",font="bold",
                   justify=RIGHT,anchor="e",borderwidth=3,relief=RIDGE)

button0=Button(master=mainFrame,text="0",bg="white",width=4,height=3,command=lambda:number(0))
button1=Button(master=mainFrame,text="1",bg="white",width=4,height=3,command=lambda:number(1))
button2=Button(master=mainFrame,text="2",bg="white",width=4,height=3,command=lambda:number(2))
button3=Button(master=mainFrame,text="3",width=4,bg="white",height=3,command=lambda:number(3))
button4=Button(master=mainFrame,text="4",width=4,height=3,bg="white",command=lambda:number(4))
button5=Button(master=mainFrame,text="5",width=4,height=3,bg="white",command=lambda:number(5))
button6=Button(master=mainFrame,text="6",width=4,height=3,bg="white",command=lambda:number(6))
button7=Button(master=mainFrame,text="7",width=4,height=3,bg="white",command=lambda:number(7))
button8=Button(master=mainFrame,text="8",width=4,height=3,bg="white",command=lambda:number(8))
button9=Button(master=mainFrame,text="9",width=4,height=3,bg="white",command=lambda:number(9))

buttonADD=Button(master=mainFrame,text="+",width=4,height=3,bg="white",command=add)
buttonSUB=Button(master=mainFrame,text="-",width=4,height=3,bg="white",command=subtract)
buttonMUL=Button(master=mainFrame,text="X",width=4,height=3,bg="white",command=multiply)
buttonDIV=Button(master=mainFrame,text="/",width=4,height=3,bg="white",command=divide)

buttonCLEAR=Button(master=mainFrame,text="C",width=4,height=3,bg="white",command=clear)
buttonEQUAL=Button(master=mainFrame,text="=",width=4,height=3,bg="white",command=equal)
buttonRECIPROCAL=Button(master=mainFrame,text="1/x",width=4,height=3,bg="white",command=reciprocal)
buttonSQRT=Button(master=mainFrame,text="√",width=4,height=3,bg="white",command=sqrt)


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
buttonRECIPROCAL.grid(row=2,column=4,padx=3,pady=3,sticky="nsew")

buttonADD.grid(row=4,column=3,padx=3,pady=3,sticky="nsew")
buttonSUB.grid(row=3,column=3,padx=3,pady=3,sticky="nsew")
buttonMUL.grid(row=2,column=3,padx=3,pady=3,sticky="nsew")
buttonDIV.grid(row=1,column=3,padx=3,pady=3,sticky="nsew")


mainFrame.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
screen_label.grid(row=0,column=0,columnspan=5,pady=10,sticky="nsew")

window.mainloop()
