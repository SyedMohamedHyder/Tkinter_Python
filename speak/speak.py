#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python

import pyttsx3
from tkinter import *


window=Tk()
window.geometry("300x400")

def sheep():

    with open ("baa baa black sheep.txt") as rhyme:

         text=rhyme.read()

    engine=pyttsx3.init()
    engine.setProperty('rate',180)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()



def twinkle():

    with open ("twinkle.txt") as rhyme:

         text=rhyme.read()

    engine=pyttsx3.init()
    engine.setProperty('rate',180)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

twinkleButton=Button(master=window,text="Click me to sing twinkle twinkle little stars rhyme",command=twinkle,bg="red",height=6)
twinkleButton.pack(pady=20,fill=X,padx=10)

sheepButton=Button(master=window,text="Click me to sing Baa Baa Black Sheep rhyme",command=sheep,height=6,bg="green")
sheepButton.pack(pady=20,fill=X,padx=10)

window.mainloop()
