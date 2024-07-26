import tkinter as tk
from tkinter import PhotoImage
import pygame
import os

def play_sound(sound_path):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()

root = tk.Tk()
root.title("Project FM [EARLY]")

# Get the current working directory
current_directory = os.getcwd()

# Construct the path to the sound and GIF relative to the current directory
sound_path = os.path.join(current_directory, "src/game/startupassets/startjingle.mp3")
logo_path = os.path.join(current_directory, "src/game/startupassets/ProjecTFMlogo.gif")

# Load the animated GIF
logo_image = PhotoImage(file=logo_path)

# Create a label to display the GIF
gif_label = tk.Label(root, image=logo_image)
gif_label.pack()

# Play the sound
play_sound(sound_path)

root.mainloop()
