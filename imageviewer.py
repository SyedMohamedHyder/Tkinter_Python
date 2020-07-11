#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python

from tkinter import *
from PIL import ImageTk,Image
import os
import sys

def forward(image_num):

    global status_label
    global num
    global img_label
    global forwardButton
    global image
    global backwardButton

    if image_num+1 == len(image)-1:

       img_label.grid_forget()
       img_label=Label(master=window,image=image[image_num+1])
       img_label.grid(row=0,column=0,columnspan=3,sticky="nsew")
       num+=1
       forwardButton["state"]=DISABLED
       status_label["text"]="Image {} of {}".format(image_num+2,len(image))
       return

    backwardButton["state"]=NORMAL
    img_label.grid_forget()
    img_label=Label(master=window,image=image[image_num+1])
    img_label.grid(row=0,column=0,columnspan=3,sticky="nsew")
    status_label["text"]="Image {} of {}".format(image_num+2,len(image))
    num+=1

def backward(image_num):

    global num
    global status_label
    global img_label
    global backwardButton
    global image
    global forwardButton

    if image_num-1 == 0:

       img_label.grid_forget()
       img_label=Label(master=window,image=image[image_num-1])
       img_label.grid(row=0,column=0,columnspan=3,sticky="nsew")
       num-=1
       status_label["text"]="Image {} of {}".format(image_num,len(image))
       backwardButton["state"]=DISABLED
       return

    forwardButton["state"]=NORMAL
    img_label.grid_forget()
    img_label=Label(master=window,image=image[image_num-1])
    num-=1
    status_label["text"]="Image {} of {}".format(image_num,len(image))
    img_label.grid(row=0,column=0,columnspan=3,sticky="nsew")

def display(image_dir):

   global image
   global status_label
   global num
   global backwardButton
   global forwardButton
   global img_label
   global window

   window=Tk()
   window.title(image_dir)
   image=[]
   num=0

   for images in os.listdir(image_dir):

       imgs=os.path.join(image_dir+images)
       img=ImageTk.PhotoImage(Image.open(imgs).convert("RGB").resize((300,300)))
       image.append(img)

   img_label=Label(master=window,image=image[num])
   img_label.grid(row=0,column=0,columnspan=3,sticky="nsew")

   forwardButton=Button(master=window,text=">>",command=lambda:forward(num))
   quitButton=Button(master=window,text="Close",command=window.quit)
   backwardButton=Button(master=window,text="<<",state=DISABLED,command=lambda:backward(num))

   status_label=Label(master=window,text="Image 1 of {}".format(len(image)),bd=3,relief=SUNKEN,anchor="e")

   backwardButton.grid(row=1,column=0,pady=10)
   quitButton.grid(row=1,column=1,sticky="ew",pady=10)
   forwardButton.grid(row=1,column=2,pady=10)

   status_label.grid(row=2,column=0,columnspan=3,sticky="ew")

   window.rowconfigure([0,1],weight=1)
   window.columnconfigure([0,1,2],weight=1)

   window.mainloop()

if __name__=="__main__":

   image_directory=sys.argv[1:]

   for directory in image_directory:
       display(directory)

