import time
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class SideRoom:
    def __init__(self):
        pass

    def storage(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Door_Closing.wav'))
        print("You walk into a small room with a few crates and notice blood on the floor")
        time.sleep(2)
        print("Over the speaker you hear: \"Please do ignore the blood and the screams. There are nothing "
              "more than mere simple experiments. I'll have my pet clean all that up shortly")
        time.sleep(3)
