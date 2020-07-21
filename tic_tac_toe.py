#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python

from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Tic Tac Toe")
window.geometry("422x416")

def check_winner():

	global all_buttons
	global condition1
	global condition2
	global condition3
	global condition4
	global condition5
	global condition6
	global condition7
	global condition8

	condition1=all_buttons[0]["text"]!="" and all_buttons[0]["text"]==all_buttons[1]["text"] and all_buttons[1]["text"]==all_buttons[2]["text"]
	condition2=all_buttons[3]["text"]!="" and all_buttons[3]["text"]==all_buttons[4]["text"] and all_buttons[4]["text"]==all_buttons[5]["text"]
	condition3=all_buttons[6]["text"]!="" and all_buttons[6]["text"]==all_buttons[7]["text"] and all_buttons[7]["text"]==all_buttons[8]["text"]
	condition4=all_buttons[0]["text"]!="" and all_buttons[0]["text"]==all_buttons[3]["text"] and all_buttons[3]["text"]==all_buttons[6]["text"]
	condition5=all_buttons[1]["text"]!="" and all_buttons[1]["text"]==all_buttons[4]["text"] and all_buttons[4]["text"]==all_buttons[7]["text"]
	condition6=all_buttons[2]["text"]!="" and all_buttons[2]["text"]==all_buttons[5]["text"] and all_buttons[5]["text"]==all_buttons[8]["text"]
	condition7=all_buttons[0]["text"]!="" and all_buttons[0]["text"]==all_buttons[4]["text"] and all_buttons[4]["text"]==all_buttons[8]["text"]
	condition8=all_buttons[2]["text"]!="" and all_buttons[2]["text"]==all_buttons[4]["text"] and all_buttons[4]["text"]==all_buttons[6]["text"]

	#print(all_buttons[0]["text"])
	return condition1 or condition2 or condition3 or condition4 or condition5 or condition6 or condition7 or condition8

# Create click function

global player
player="X"

def click(index):

	global player

	if player=="X":

		all_buttons[index].config(text="X",state=DISABLED)
		player="O"
		winner="X"


	else:

		all_buttons[index].config(text="O",state=DISABLED)
		player="X"
		winner="O"

	#print(all_buttons[0]["text"])

	if check_winner():

		messagebox.showinfo("Victory!","Player {} wins the game".format(winner))

		for button in all_buttons:

			button.config(state=DISABLED) 

		if condition1:

			button1.config(bg="#90EE90",fg="white")
			button2.config(bg="#90EE90",fg="white")
			button3.config(bg="#90EE90",fg="white")

		elif condition2:

			button4.config(bg="#90EE90",fg="white")
			button5.config(bg="#90EE90",fg="white")
			button6.config(bg="#90EE90",fg="white")

		elif condition3:

			button7.config(bg="#90EE90",fg="white")
			button8.config(bg="#90EE90",fg="white")
			button9.config(bg="#90EE90",fg="white")

		elif condition4:

			button1.config(bg="#90EE90",fg="white")
			button4.config(bg="#90EE90",fg="white")
			button7.config(bg="#90EE90",fg="white")

		elif condition5:

			button2.config(bg="#90EE90",fg="white")
			button5.config(bg="#90EE90",fg="white")
			button8.config(bg="#90EE90",fg="white")

		elif condition6:

			button3.config(bg="#90EE90",fg="white")
			button6.config(bg="#90EE90",fg="white")
			button9.config(bg="#90EE90",fg="white")

		elif condition7:

			button1.config(bg="#90EE90",fg="white")
			button5.config(bg="#90EE90",fg="white")
			button9.config(bg="#90EE90",fg="white")

		elif condition8:

			button3.config(bg="#90EE90",fg="white")
			button5.config(bg="#90EE90",fg="white")
			button7.config(bg="#90EE90",fg="white")




# Create buttons 

button1=Button(master=window,width=15,height=7,font="bold",command=lambda:click(0))
button2=Button(master=window,width=15,height=7,font="bold",command=lambda:click(1))
button3=Button(master=window,width=15,height=7,font="bold",command=lambda:click(2))
button4=Button(master=window,width=15,height=7,font="bold",command=lambda:click(3))
button5=Button(master=window,width=15,height=7,font="bold",command=lambda:click(4))
button6=Button(master=window,width=15,height=7,font="bold",command=lambda:click(5))
button7=Button(master=window,width=15,height=7,font="bold",command=lambda:click(6))
button8=Button(master=window,width=15,height=7,font="bold",command=lambda:click(7))
button9=Button(master=window,width=15,height=7,font="bold",command=lambda:click(8))

all_buttons=[button1,button2,button3,button4,button5,button6,button7,button8,button9]

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)

window.mainloop()