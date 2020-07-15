#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python

import os
from PIL import Image,ImageTk
import tkinter as tk
import random
from tkinter import messagebox





window=tk.Tk()
window.iconbitmap("flag.ico")
window.title("Indian States Game")
window.geometry("400x705")
window.resizable(False,True)


all_states_list=[]
user_capital=tk.StringVar()


for state in os.listdir("states/"):

    all_states_list.append(os.path.splitext(state)[0])

imageFrame=tk.Frame(master=window)
statusFrame=tk.Frame(master=window)
capitalFrame=tk.Frame(master=window)
status_capital_Frame=tk.Frame(master=window)

total=10

user_total=0

capital={"andhra pradesh":"amaravati",
"arunachal pradesh":"itanagar",
"assam":"dispur",
"bihar":"patna",
"chandigarh":"chandigarh",
"chhattisgarh":"raipur",
"dadra and nagar haveli":"daman",
"daman and diu":"daman",
"delhi":"new Delhi",
"goa":"panaji",
"gujarat":"gandhinagar",
"haryana":"chandigarh",
"himachal pradesh":"shimla",
"jammu and kashmir":"srinagar",
"jharkhand":"ranchi",
"karnataka":"bengaluru",
"kerala":"thiruvananthapuram",
"madhya pradesh":"bhopal",
"maharashtra":"mumbai",
"manipur":"imphal",
"meghalaya":"shillong",
"mizoram":"aizawl",
"nagaland":"kohima",
"orissa":"bhubaneswar",
"pondichery":"pondicherry",
"punjab":"chandigarh",
"rajasthan":"jaipur",
"sikkim":"gangtok",
"tamil nadu":"chennai",
"telangana":"hyderabad",
"tripura":"agartala",
"uttar pradesh":"lucknow",
"uttarakhand":"dehradun",
"west bengal":"kolkata"}



def hide_all_frames():

    all_frame=[imageFrame,capitalFrame,statusFrame,status_capital_Frame]

    for frame in all_frame:

        for widget in frame.winfo_children():

            widget.destroy()

        frame.grid_forget()


def capital_answer(all_stato):

    global user_total

    if user_capital.get().lower()==capital[state]:

       hintLabel["text"]=""
       hintLabel.grid(row=1,column=1)

       submitLabel["text"]="Correct!"
       submitLabel.grid(row=7,column=1)

       user_total+=1

       if user_total==total:
          hide_all_frames()
          messagebox.showinfo("GAME OVER","WINNER WINNER CHICKEN DINNER!")

       else:

          status_capital_Label=tk.Label(master=status_capital_Frame,text="You have solved {} out of {}".format(user_total,total))
          status_capital_Label.grid(row=0,column=0,sticky="e",padx=5)
          #del all_stato[rando]
          submitButton.configure(state="disabled")
          next_capital_Button=tk.Button(master=capitalFrame,text="Next",command=lambda:capitals(all_stato))
          next_capital_Button.grid(row=8,column=1,padx=3,pady=2)



    else:

       hintLabel["text"]="The given state is {}".format(state.title())
       hintLabel.grid(row=1,column=1)

       submitLabel["text"]="Incorrect ! Try Again"
       submitLabel.grid(row=7,column=1)



def capitals(all_statos):

    global all_states_list
    global capitalFrame
    global img
    global user_capital
    global state
    global submitLabel
    global hintLabel
    global rando
    global status_capital_Frame
    global status_capital_Label
    global submitButton

    hide_all_frames()

    option_states=[]

    rando=random.randint(0,len(all_statos)-1)
    state=all_statos[rando]

    image_path="states/"+state+(".png")

    option_states.append(capital[state])

    while len(option_states) < 3 :

        new_state=all_states_list[random.randint(0,len(all_states_list)-1)]

        if capital[new_state] in option_states:

           continue

        else:

           option_states.append(capital[new_state])


    random.shuffle(option_states)


    image_path="states/"+state+(".png")

    img=ImageTk.PhotoImage(Image.open(image_path))

    capitalFrame=tk.Frame(master=window)
    capitalFrame.grid(row=0,column=0,sticky="nsew")

    capitalLabel=tk.Label(master=capitalFrame,image=img)
    capitalLabel.grid(row=0,column=0,pady=5,columnspan=3)


    user_capital.set(None)

    for index,option in enumerate(option_states):

        optionButton=tk.Radiobutton(master=capitalFrame,text=option,variable=user_capital,value=option)
        optionButton.grid(row=index+2,column=1,pady=3)

    submitButton=tk.Button(master=capitalFrame,text="Answer",width=50,command=lambda:capital_answer(all_statos))
    submitButton.grid(row=5,column=1,sticky="we",pady=5)

    submitLabel=tk.Label(master=capitalFrame,text="")
    submitLabel.grid(row=7,column=1)

    skipButton=tk.Button(master=capitalFrame,text="Pass",command=lambda:capitals(all_statos))
    skipButton.grid(row=6,column=1,pady=5)

    hintLabel=tk.Label(master=capitalFrame,text="")
    hintLabel.grid(row=1,column=1)


    status_capital_Frame=tk.Frame(master=window,relief="sunken",bd=3)
    status_capital_Frame.grid(row=1,column=0,sticky="we")

    status_capital_Label=tk.Label(master=status_capital_Frame,text="You have solved {} out of {}".format(user_total,total))
    status_capital_Label.grid(row=0,column=0,padx=5)


def state_answer(all_state):

    global user_total

    answer=answerEntry.get().lower().replace(" ","")

    if state.replace(" ","")==answer:

       answerLabel["text"]="Correct!"
       answerLabel.grid(row=4,column=1)

       user_total+=1

       if user_total==total:
          hide_all_frames()
          messagebox.showinfo("GAME OVER","WINNER WINNER CHICKEN DINNER!")
       else:
          statusLabel=tk.Label(master=statusFrame,text="You have solved {} out of {}".format(user_total,total))
          statusLabel.grid(row=0,column=0,sticky="e",padx=5)
          del all_state[rando]
          answerButton.configure(state="disabled")
          nextButton=tk.Button(master=imageFrame,text="Next",command=lambda:states(all_state))
          nextButton.grid(row=5,column=1,padx=10,pady=5)

    else:
       answerLabel["text"]="Incorrect ! Try Again"
       answerLabel.grid(row=4,column=1)

def states(all_states):

    global imageFrame
    global rando
    global img
    global state
    global answerEntry
    global answerLabel
    global statusFrame
    global answerButton


    hide_all_frames()

    rando=random.randint(0,len(all_states)-1)
    state=all_states[rando]
    image_path="states/"+state+(".png")

    img=ImageTk.PhotoImage(Image.open(image_path))

    imageFrame=tk.Frame(master=window)
    imageFrame.grid(row=0,column=0,sticky="nsew")


    stateLabel=tk.Label(master=imageFrame,image=img)
    stateLabel.grid(row=0,column=0,pady=5,columnspan=3)

    answerEntry=tk.Entry(master=imageFrame)
    answerEntry.grid(row=1,column=1,pady=10,sticky="ew")

    passButton=tk.Button(master=imageFrame,text="Pass",command=lambda:states(all_states))
    passButton.grid(row=2,column=1,padx=5)

    answerButton=tk.Button(master=imageFrame,text="Answer",command=lambda:state_answer(all_states))
    answerButton.grid(row=3,column=1,pady=10,sticky="ew")

    statusFrame=tk.Frame(master=window,relief="sunken",bd=3)
    statusFrame.grid(row=1,column=0,sticky="we")

    statusLabel=tk.Label(master=statusFrame,text="You have solved {} out of {}".format(user_total,total))
    statusLabel.grid(row=0,column=0,padx=10)

    answerLabel=tk.Label(master=imageFrame,text="")
    answerLabel.grid(row=4,column=1)

mymenu=tk.Menu(window)
window.config(menu=mymenu)

geomenu=tk.Menu(mymenu)
mymenu.add_cascade(label="Geography",menu=geomenu)
geomenu.add_command(label="States",command=lambda:states(all_states_list))
geomenu.add_command(label="State Capitals",command=lambda:capitals(all_states_list))
geomenu.add_separator()
geomenu.add_command(label="Exit",command=window.quit)

window.mainloop()
