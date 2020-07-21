#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python

# Import all modules 

from tkinter import *
import pygame
from tkinter import filedialog
import os
import time
from mutagen.mp3 import MP3
from tkinter import ttk
from PIL import ImageTk,Image

window=Tk()
window.title("MP3 Player")
window.geometry("500x430")
window.resizable(False,False)

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

global stopped
stopped=False

def stop():

	global paused
	global playing

	paused=False
	pygame.mixer.music.stop()
	song_box.selection_clear(0,END)
	#song_box.activate(None)

	# Clear the statusbar when stopped
	status_bar.config(text="")

	# When stopped a song the slider should go to the value of 0
	music_slider.config(value=0)

	global stopped

	playing=False
	stopped=True

# Create a slide function which reacts upon the movement slider

def slide(event):

	global song
	global paused
	#global current_time

	if stopped or not playing:

		return

	# When the slider is moved , get its value and start the song from there

	#current_time=music_slider.get()

	#song_number=song_box.curselection()[0]
	#song_name=song_box.get(song_number)
	#song_path=song_path_list[song_number]
	#song_extension=".mp3"
	#song="{}/{}{}".format(song_path,song_name,song_extension)

	paused=False
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0,start=int(music_slider.get()))

# Create function to update playtime

def playtime():

	if stopped:

		return

	global current_time
	global formatted_song_length
	global paused

	current_time=int(pygame.mixer.music.get_pos() / 1000)
	formatted_current_time=time.strftime("%H:%M:%S",time.gmtime(current_time))

	global song_path_list

	#paused=False (Big Error)

	if not song_box.curselection():

		return

	#song_number=song_box.curselection()[0]
	#song_name=song_box.get(song_number)
	#song_path=song_path_list[song_number]
	#song_extension=".mp3"
	#song="{}/{}{}".format(song_path,song_name,song_extension)

	#song_muta=MP3(song)
	#song_length=int(song_muta.info.length)
	#formatted_song_length=time.strftime("%H:%M:%S",time.gmtime(song_length))

	if int(music_slider.get()) == song_length:

		music_slider.config(value=song_length)
		#formatted_new_time=time.strftime("%H:%M:%S",time.gmtime(music_slider.get()))
		status_bar.config(text="Time elapsed : {} of Total time : {}".format(formatted_song_length,formatted_song_length))

	elif paused:

		pass

	# Check whether the slider and current_time are moving together

	elif int(music_slider.get()) == current_time:

		music_slider.config(value=current_time)
		status_bar.config(text="Time elapsed : {} of Total time : {}".format(formatted_current_time,formatted_song_length))


	else:

		music_slider.config(value=int(music_slider.get()))
		formatted_new_time=time.strftime("%H:%M:%S",time.gmtime(int(music_slider.get())))
		status_bar.config(text="Time elapsed : {} of Total time : {}".format(formatted_new_time,formatted_song_length))
		next_time=int(music_slider.get())+1
		music_slider.config(value=next_time)

	# Update the 'to' value of music_slider to the song_length

	#music_slider.config(value=current_time)

	#dummy_label.config(text=f"{int(music_slider.get())}   {current_time}")

	#status_bar.config(text="Time elapsed : {} of Total time : {}".format(formatted_current_time,formatted_song_length))

	# Update status bar every second

	status_bar.after(1000,playtime)


# Function to play a song

global playing
playing=False

def play():

	global stopped
	global song_path_list
	global paused
	global song
	global playing

	stopped=False
	paused=False

	if not song_box.curselection():
		return

	music_slider.config(value=0)

	song_number=song_box.curselection()[0]
	song_name=song_box.get(song_number)
	song_path=song_path_list[song_number]
	song_extension=".mp3"
	song="{}/{}{}".format(song_path,song_name,song_extension)

	# Start music

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	global formatted_song_length
	global song_length

	song_muta=MP3(song)
	song_length=int(song_muta.info.length)
	formatted_song_length=time.strftime("%H:%M:%S",time.gmtime(song_length))

	music_slider.config(to=song_length)

	#song_box.config(state=DISABLED)

	# Call playtime function which updates the playtime every second
	if playing:

		return

	playtime()
	playing=True

def backward():

	global song_path_list
	global paused
	global song
	global stopped
	global playing

	stopped=False
	paused=False

	if not song_box.curselection():
		return

	music_slider.config(value=0)

	previous_song_num=song_box.curselection()[0]-1

	if previous_song_num < 0 :

		return

	previous_song_name=song_box.get(previous_song_num)
	previous_song_path=song_path_list[previous_song_num]
	song_extension=".mp3"
	song="{}/{}{}".format(previous_song_path,previous_song_name,song_extension)

	# Start music
	song_box.selection_clear(0,END)
	song_box.activate(previous_song_num)
	song_box.selection_set(previous_song_num,last=None)

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	global formatted_song_length
	global song_length

	song_muta=MP3(song)
	song_length=int(song_muta.info.length)
	formatted_song_length=time.strftime("%H:%M:%S",time.gmtime(song_length))

	music_slider.config(to=song_length)

	if playing:

		return

	playtime()
	playing=True

def forward():

	global song_path_list
	global paused
	global song
	global stopped
	global playing

	paused=False
	stopped=False

	if not song_box.curselection():
		return

	music_slider.config(value=0)

	next_song_num=song_box.curselection()[0]+1

	if next_song_num > song_box.size()-1 :

		return

	next_song_name=song_box.get(next_song_num)
	next_song_path=song_path_list[next_song_num]
	song_extension=".mp3"
	song="{}/{}{}".format(next_song_path,next_song_name,song_extension)

	# Start music
	song_box.selection_clear(0,END)
	song_box.activate(next_song_num)
	song_box.selection_set(next_song_num,last=None)

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	global formatted_song_length
	global song_length

	song_muta=MP3(song)
	song_length=int(song_muta.info.length)
	formatted_song_length=time.strftime("%H:%M:%S",time.gmtime(song_length))

	music_slider.config(to=song_length)

	if playing:

		return

	playtime()
	playing=True

def delete_song():

	global song_path_list

	if  not song_box.curselection():
		return

	song_to_be_deleted=song_box.curselection()[0]
	song_box.delete(song_to_be_deleted)
	del song_path_list[song_to_be_deleted]
	stop()

def delete_many_songs():

	global song_path_list

	song_box.delete(0,END)
	song_path_list=[]
	stop()

def volume(event):

	global volume_level
	global volume_meter
	# Change volume according to the volume_meter value
	# pygame has a volume range of 0 to 1
	volume_level=volume_meter.get()
	pygame.mixer.music.set_volume(volume_level)
	#dummy_label.config(text=volume_meter.get()*100)

global volume_level
volume_level=1

def display_volume_meter():

	global volume_level
	global display
	global volume_meter

	if display:

		# Create volume_meter scale 
		volume_meter=ttk.Scale(master=volumeFrame,from_=0,to=1,orient=HORIZONTAL,value=volume_level,command=volume)
		volume_meter.grid(row=1,column=1,sticky="w")
		display=False

	else:

		volume_meter.grid_forget()
		display=True


# Create menus for our window

player_menu=Menu(window)
window.config(menu=player_menu)

# Create an add menu which can add songs to our listbox
add_menu=Menu(player_menu)
player_menu.add_cascade(label="Add Song",menu=add_menu)

add_menu.add_command(label="Add One Song",command=add_song)
add_menu.add_command(label="Add Multiple Songs",command=add_many_songs)

# Create a delete menu which can delete songs in our list box

delete_menu=Menu(player_menu)
player_menu.add_cascade(label="Delete Song",menu=delete_menu)

delete_menu.add_command(label="Delete Selected Song",command=delete_song)
delete_menu.add_command(label="Delete All Songs",command=delete_many_songs)

# Create a frame to add scrollbar

song_boxFrame=Frame(master=window)
song_boxFrame.pack(pady=20,padx=20)

# Create a scroll_bar

song_box_scrollbar=Scrollbar(master=song_boxFrame,orient=VERTICAL)
song_box_scrollbar.pack(side=RIGHT,fill=Y)

# Create a song box 

song_box=Listbox(master=song_boxFrame,bg="white",fg="black",width=75,selectbackground="black",selectforeground="white",activestyle="none",font=("Arial",10),yscrollcommand=song_box_scrollbar.set)
song_box.pack()

# Configure our scrollbar

song_box_scrollbar.config(command=song_box.yview)

# Load images for our buttons 

pause_image=PhotoImage(file="c:/Users/SYED/Desktop/RaspberryPi/mp3player/button_images/pause.png")
stop_image=PhotoImage(file="c:/Users/SYED/Desktop/RaspberryPi/mp3player/button_images/stop.png")
play_image=PhotoImage(file="c:/Users/SYED/Desktop/RaspberryPi/mp3player/button_images/play.png")
forward_image=PhotoImage(file="c:/Users/SYED/Desktop/RaspberryPi/mp3player/button_images/forward.png")
backward_image=PhotoImage(file="c:/Users/SYED/Desktop/RaspberryPi/mp3player/button_images/backward.png")
volume_image=ImageTk.PhotoImage(Image.open("c:/Users/SYED/Desktop/RaspberryPi/mp3player/button_images/volume.jpg"))

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

forward_button=Button(master=buttonFrame,image=forward_image,bd=0,command=forward)
forward_button.grid(row=0,column=4,padx=10)

backward_button=Button(master=buttonFrame,image=backward_image,bd=0,command=backward)
backward_button.grid(row=0,column=0,padx=10)

# Create volume Frame

volumeFrame=Frame(master=window)
volumeFrame.pack()

# Create slider

music_slider=ttk.Scale(master=volumeFrame,from_=0,to=100,orient=HORIZONTAL,value=0,length=400,command=slide)
music_slider.grid(row=0,column=0,pady=(40,20),columnspan=13)

global display
display=True
# Create volume Button

volumeButton=Button(master=volumeFrame,image=volume_image,bd=0,command=display_volume_meter)
volumeButton.grid(row=1,column=0,sticky="w")

# Create status bar

status_bar=Label(master=window,text="",bd=1,relief="groove",anchor="e")
status_bar.pack(fill=X,ipady=3,side=BOTTOM)

# Create a dummy label for analysis

#dummy_label=Label(master=window,text="")
#dummy_label.pack()


window.mainloop()