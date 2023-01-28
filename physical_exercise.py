import pygame
from pygame import mixer
import time

def getdate():
    import datetime
    return datetime.datetime.now()

mixer.init()

mixer.music.load("C:\\Users\prati\Downloads\Exercise.mp3")

mixer.music.set_volume(0.8)

mixer.music.play()
print("music started playing-------")

while(True):
    print("------------------------------------------------------------")
    print("Enter done to stop playing")

    user_input = input(" ")
    if user_input == "done":
        mixer.music.stop()
        print("music stopped playing")
        print(str(getdate()))
        break
