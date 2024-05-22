# project7
simple music player application using python 
by: mohamed fares
This module provides a simple music player application built using the Pygame and Tkinter libraries.

The `playsong()` function is responsible for loading and playing the currently selected song from the playlist. 
It retrieves the name of the currently selected song, loads it using the Pygame mixer, and sets the song status to "Playing".

The `pausesong()` function pauses the currently playing song and sets the song status to "Paused".

The `stopsong()` function stops the currently playing song and sets the song status to "Stopped".

The `resumesong()` function resumes the currently paused song and sets the song status to "Resuming".

The main part of the code sets up the Tkinter GUI, initializes the Pygame mixer, and populates the playlist with songs from a specifie
