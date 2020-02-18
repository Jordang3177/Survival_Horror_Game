from Sound_Files.sounds import _Sounds as Sounds
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class SideRoom:
    def __init__(self):
        self.returning = False

    def storage(self):
        pygame.mixer.Channel(1).play(Sounds.door_closing(self))
        print("You walk into a small room with a few crates and notice blood on the floor")
        time.sleep(2)
        print("Over the speaker you hear: \"Please do ignore the blood and the screams. They are nothing "
              "more than mere simple experiments. I'll have my pet clean all that up shortly")
        time.sleep(3)
        print("As you move forward you hear a small clicking noise, but nothing seems to happen")
        time.sleep(3)
        response = input("Do you (Inspect) or (Leave) the room: ")
        while response.lower() != 'inspect' and response.lower() != 'leave':
            response = input("Please enter either Inspect or Leave: ")
        if response.lower() == 'inspect':
            self.returning = True
            print("You look around the room and notice some strange markings on the wall.")
            time.sleep(3)
            print("There appears to be fresh blood on the walls with claw marks all around them")
            time.sleep(3)
            print("You notice nothing else and begin to leave the room")
            pygame.mixer.Channel(1).play(Sounds.door_squeak(self))
            return
        if response.lower() == 'leave':
            self.returning = True
            print("You leave the room")
            pygame.mixer.Channel(1).play(Sounds.door_squeak(self))
            return

    def returning_checker(self):
        return self.returning