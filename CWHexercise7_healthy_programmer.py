# IT IS A PROGRAM FOR HEALTHY PROGRAMMER IN WHICH PROGRAMMER IS REMEMBERED TO DRINK WATER IN EVERY 40 MINS , EYES EXERCISE IN EVERY 30 MINS AND PHYSICAL EXERCISE IN EVERY 45 MINS

# Prerequisite :
#  a water.mp3 file
#  a eye.mp3 file
#  a excersise.mp3 file
# in your downloads

from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break


def lognow(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()} \n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_excercise = time()
    watersecs = 40*60
    eyessecs = 30*60
    excercisesecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("Water drinking time. Enter 'drank ' to stop")
            musiconloop('C:\\Users\prati\Downloads\SBXCMQR-water-pouring-into-water.mp3', 'drank')
            init_water = time()
            lognow("Water drank at")

        if time() - init_eyes > eyessecs:
            print("Eye excerise time. Enter 'done' to stop")
            musiconloop('C:\\Users\prati\Downloads\Starry Eye.mp3', 'done')
            init_eyes = time()
            lognow("Eye relaxed at ")

        if time() - init_excercise > excercisesecs:
            print("excersise time . Enter 'donephy' to stop")
            musiconloop('C:\\Users\prati\Downloads\Exercise.mp3', 'donephy')
            init_excercise = time()
            lognow("Physical excercise done  at ")
