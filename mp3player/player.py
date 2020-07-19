#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python

from tkinter import *
import pygame
from tkinter import filedialog
import os

window=Tk()
window.title("MP3 Player")
window.geometry("500x300")

song_path_list=[]
paused=False

# Initialize pygame

pygame.mixer.init()

# Function to add many songs at a time

def add_many_songs():

	songs=filedialog.askopenfilenames(initialdir="c:/Users/SYED/Desktop/RaspberryPi/mp3player/songs/",
		filetypes=[("*.mp3","mp3 Files")])

	if not songs:
		return

	global song_path_list

	for song in songs:

		song_path_list.append(os.path.split(song)[0])
		song_name=os.path.splitext(os.path.basename(song))[0]
		song_box.insert(END,song_name)

# Function to add one song

def add_song():

	# Ask user for the song
	song=filedialog.askopenfilename(initialdir="c:/Users/SYED/Desktop/RaspberryPi/mp3player/songs/",
		filetypes=[("*.mp3","mp3 Files")])
	
	if not song:
		return

	# Adding only song name to display in the listbox

	global song_path_list

	song_path_list.append(os.path.split(song)[0])
	song_name=os.path.splitext(os.path.basename(song))[0]
	song_box.insert(END,song_name)

def pause(song_paused):

	global paused

	if song_paused:

		pygame.mixer.music.unpause()
		paused=False

	else:

		pygame.mixer.music.pause()
		paused=True


# Function to stop the music

def stop():
	
	global paused

	paused=False
	pygame.mixer.music.stop()
	song_box.selection_clear(ACTIVE)

# Function to play a song

def play():

	global song_path_list
	global paused

	paused=False

	if not song_box.curselection():
		return

	song_number=song_box.curselection()[0]
	song_name=song_box.get(ANCHOR)
	song_path=song_path_list[song_number]
	song_extension=".mp3"
	song="{}/{}{}".format(song_path,song_name,song_extension)

	# Start music

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)


# Create menus for our window

player_menu=Menu(window)
window.config(menu=player_menu)

# Create an add menu which can add songs to our listbox
add_menu=Menu(player_menu)
player_menu.add_cascade(label="Add Song",menu=add_menu)

add_menu.add_command(label="Add One Song",command=add_song)
add_menu.add_command(label="Add Multiple Songs",command=add_many_songs)

# Create a song box 

song_box=Listbox(master=window,bg="black",fg="white",width=75,selectbackground="white",selectforeground="green")
song_box.pack(pady=20,padx=20)

# Load images for our buttons 

pause_image=PhotoImage(file="c:/Users/SYED/Desktop/RaspberryPi/mp3player/button_images/pause.png")
stop_image=PhotoImage(file="c:/Users/SYED/Desktop/RaspberryPi/mp3player/button_images/stop.png")
play_image=PhotoImage(file="c:/Users/SYED/Desktop/RaspberryPi/mp3player/button_images/play.png")
forward_image=PhotoImage(file="c:/Users/SYED/Desktop/RaspberryPi/mp3player/button_images/forward.png")
backward_image=PhotoImage(file="c:/Users/SYED/Desktop/RaspberryPi/mp3player/button_images/backward.png")

# Create a Frame to hold all the Buttons

buttonFrame=Frame(master=window)
buttonFrame.pack()

# Add Buttons to the buttonFrame

pause_button=Button(master=buttonFrame,image=pause_image,bd=0,command=lambda:pause(paused))
pause_button.grid(row=0,column=1,padx=10)

stop_button=Button(master=buttonFrame,image=stop_image,bd=0,command=stop)
stop_button.grid(row=0,column=3,padx=10)

play_button=Button(master=buttonFrame,image=play_image,bd=0,command=play)
play_button.grid(row=0,column=2,padx=10)

forward_button=Button(master=buttonFrame,image=forward_image,bd=0)
forward_button.grid(row=0,column=4,padx=10)

backward_button=Button(master=buttonFrame,image=backward_image,bd=0)
backward_button.grid(row=0,column=0,padx=10)


window.mainloop()