import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class _Sounds:
    def agony_scream(self):
        return pygame.mixer.Sound('Sound_Files/Agony_Scream.wav')

    def bones(self):
        return pygame.mixer.Sound('Sound_Files/Bones.wav')

    def door_closing(self):
        return pygame.mixer.Sound('Sound_Files/Door_Closing.wav')

    def door_squeak(self):
        return pygame.mixer.Sound('Sound_Files/DoorSqueak.wav')

    def evil_laugh(self):
        return pygame.mixer.Sound('Sound_Files/Evil_Laugh.wav')

    def others_sound(self):
        return pygame.mixer.Sound('Sound_Files/Others_Sound.wav')

    def side_door_gone(self):
        return pygame.mixer.Sound('Sound_Files/Side_Door_Gone.wav')

    def others_bite(self):
        return pygame.mixer.Sound('Sound_Files/Others_Bite.wav')

    def others_breathing(self):
        return pygame.mixer.Sound('Sound_Files/Others_Breathing.wav')

    def others_laugh(self):
        return pygame.mixer.Sound('Sound_Files/Others_Laugh.wav')