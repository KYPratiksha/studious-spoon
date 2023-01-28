import pygame
from pygame import mixer
import time
def getdate():
    import datetime
    return datetime.datetime.now()

# Instantiate mixer
mixer.init()

# Load audio file
mixer.music.load("C:\\Users\prati\Downloads\SBXCMQR-water-pouring-into-water.mp3")
# time.sleep(2)
print("music started playing....")

# Set preferred volume
mixer.music.set_volume(0.2)

# Play the music
mixer.music.play()

# Infinite loop
while True:
    print("------------------------------------------------------------------------------------")
    print("Enter 'done' to exit the program")

    # take user input
    userInput = input(" ")

    if userInput == 'done':

        # Stop the music playback
        mixer.music.stop()
        print("music is stopped....")
        print(str(getdate()))
        # break




