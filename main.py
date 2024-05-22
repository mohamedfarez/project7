"""
by: mohamed fares
This module provides a simple music player application built using the Pygame and Tkinter libraries.

The `playsong()` function is responsible for loading and playing the currently selected song from the playlist. It retrieves the name of the currently selected song, loads it using the Pygame mixer, and sets the song status to "Playing".

The `pausesong()` function pauses the currently playing song and sets the song status to "Paused".

The `stopsong()` function stops the currently playing song and sets the song status to "Stopped".

The `resumesong()` function resumes the currently paused song and sets the song status to "Resuming".

The main part of the code sets up the Tkinter GUI, initializes the Pygame mixer, and populates the playlist with songs from a specified directory. It also creates the buttons for playing, pausing, stopping, and resuming the songs.
"""
import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()    

root=Tk()
root.title('Project(mohamed fares) Music player project')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#playlist---------------

playlist=Listbox(root,selectmode=SINGLE,bg="DodgerBlue2",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\BOSS\Desktop\MyPlaylist')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="play",command=playsong)
playbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)

mainloop()