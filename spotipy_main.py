# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 15:59:37 2023

@author: Tom
"""
#other files
from spotify_auth import *

#spoitipy libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

#Arduino libraries

import serial

#tkinter window
import tkinter as tk
import threading

arduino = serial.Serial(port = 'COM3', baudrate = 9600 , timeout = .1)
scope = "user-modify-playback-state user-read-playback-state"  # Permission scope for controlling playback
#read_scope = "user-read-playback-state"
os.environ["SPOTIPY_CLIENT_ID"] = client_id
os.environ["SPOTIPY_CLIENT_SECRET"] = client_secret
os.environ["SPOTIPY_REDIRECT_URI"] = 'http://localhost:8888/callback'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
#sp_read = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=read_scope))

def myround(x, base=5):
    return base * round(x/base)

def next_song():
       sp.next_track()
       print("Skipping to the next song.")

def prev_song():
    sp.previous_track()
    print("Rewinding to the last song.")
    
def current_song():
    current_track = sp.current_playback()
    
    if current_track:
        print(current_track["item"]["name"])
    else:
        print('No song is currently playing.')
        
def pause_play():
    current_track = sp.current_playback()
    if current_track['is_playing']:
        sp.pause_playback()
        print('Playback paused.')
    else:
        sp.start_playback()
        print('Playback resumed.')

def reduce_volume():
    current_track = sp.current_playback()
    if current_track is None:
        print("No song is currently playing.")
    else:
        volume_percent = current_track["device"]["volume_percent"]
        new_volume = min(volume_percent - 5, 100)  # Increase volume by 10 percent (capped at 100)
        new_volume = int(myround(new_volume,base=5))
        sp.volume(new_volume)
        print(f"Volume reduced to {new_volume}%")

def increase_volume():
    current_track = sp.current_playback()
    if current_track is None:
        print("No song is currently playing.")
    else:
        volume_percent = current_track["device"]["volume_percent"]
        new_volume = min(volume_percent + 5, 100)  # Increase volume by 10 percent (capped at 100)
        new_volume = int(myround(new_volume,base=5))
        sp.volume(new_volume)
        print(f"Volume increased to {new_volume}%")
        
        
        
def main_script():


    x = arduino.readline().decode().strip()

    if x == 'Pressed on next song button':
        next_song()
    if x == 'Pressed on button play/pause':
        pause_play()
    if x == 'Pressed on last song button':
        prev_song()
    if x == "Pressed on volume up button":
        increase_volume()
    if x == "Pressed on volume down button":
        reduce_volume()
        
    
    if not script_stopped:
         root.after(500, main_script)

        





if __name__ == '__main__':
    def on_close():
        global script_stopped
        script_stopped = True
        root.destroy()
        arduino.close()
        script_thread.join()
    script_stopped = False        
    script_thread = threading.Thread(target = main_script)
    script_thread.start()

    root = tk.Tk()
    root.geometry('400x200')
    root.title('Spotify bot')
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
        