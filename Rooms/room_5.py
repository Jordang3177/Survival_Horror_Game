import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from Sound_Files.sounds import _Sounds as Sounds

class Room5:
    def __init__(selfs):
        pass

    def room_5(self):
        pygame.mixer.Channel(4).play(Sounds.door_closing(self))
        print("You enter into a room with nothing in it but two doors and a piano in the corner of the room")