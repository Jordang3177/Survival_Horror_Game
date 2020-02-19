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

    def body_falling(self):
        return pygame.mixer.Sound('Sound_Files/Body_Falling.wav')

    def glass_breaking(self):
        return pygame.mixer.Sound('Sound_Files/Glass_Breaking.wav')

    def others_moving(self):
        return pygame.mixer.Sound('Sound_Files/Others_Moving.wav')

    def far_away_movement(self):
        return pygame.mixer.Sound('Sound_Files/Far_Away_Movement.wav')

    def metal_door_opening(self):
        return pygame.mixer.Sound('Sound_Files/Metal_Door_Opening.wav')

    def footsteps_on_metal(self):
        return pygame.mixer.Sound('Sound_Files/Footsteps_On_Metal.wav')

    def cutting_rope(self):
        return pygame.mixer.Sound('Sound_Files/Cutting_Rope.wav')