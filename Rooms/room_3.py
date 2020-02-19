import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from Sound_Files.sounds import _Sounds as Sounds

class Room3:
    def __init__(self):
        self.baby_key = False
        self.scared = False

    def room_3(self):
        print("As you walk into the room you see a statue of a man holding a baby")
        time.sleep(3)
        print("At the other side of the room there is another door")
        response = input("Do you go to the (Statue) or to the (Door): ")
        while response.lower() != 'statue' and response.lower() != 'door':
            response = input("Please enter either Statue or Door: ")
        if response.lower() == 'statue':
            print("You look upon the statue and notice that there is a small thing on the baby")
            time.sleep(3)
            response = input("Do you (Take) it or (Leave) it: ")
            while response.lower() != 'take' and response.lower() != 'leave':
                response = input("Please enter either Take or Leave: ")
            if response.lower() == 'take':
                self.baby_key = True
                print("You take what seems to be a small key with an insignia of a clock")
                time.sleep(3)
                print("As you take it you hear a moving sound far away")
                time.sleep(3)
                pygame.mixer.Channel(2).play(Sounds.far_away_movement(self))
                response = input("Do you leave to the (Door) or put the key (Back): ")
                while response.lower() != 'door' and response.lower() != 'back':
                    response = print("Please enter either Door or Back: ")
                if response.lower() == 'back':
                    self.baby_key = False
                    print("You put the key back where it was and hear the same moving sound as before ")
                    pygame.mixer.Channel(3).play(Sounds.far_away_movement(self))
                    time.sleep(3)
                    response = 'door'
        if response.lower() == 'door':
            print("You walk over to the door ")
            time.sleep(3)
            print("Behind you you hear something calling out to you and what feels like your name being called")
            time.sleep(3)
            response = input("Do you (Inspect) the door, open the door (Slow), or open the door (Fast): ")
            while response.lower() != 'inspect' and response.lower() != 'slow' and response.lower() != 'fast':
                response = input("Please enter Inspect, Slow, or Fast: ")
            if response.lower() == 'inspect':
                print("The door has a symbol of a pig inscribed near the top of the door: ")
                time.sleep(3)
                response = input("Do you open the door (Slow), or open the door (Fast): ")
            if response.lower() == 'slow':
                print("You open the door as calmly as if nothing had just happened behind you and walk to the next room")
                pygame.mixer.Channel(1).play(Sounds.door_squeak(self))
                time.sleep(3)
                return
            if response.lower() == 'fast':
                self.scared = True
                print("You open the door as fast as you can and run into the next room terrified.")
                print("Behind you hearing the laughter of something wicked.")
                pygame.mixer.Channel(3).play(Sounds.others_laugh(self))
                pygame.mixer.Channel(2).play(Sounds.door_squeak(self))
                time.sleep(3)
                return

    def baby_key_checker(self):
        return self.baby_key

    def scared_checker(self):
        return self.scared