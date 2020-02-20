import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from Sound_Files.sounds import _Sounds as Sounds

class Room5:
    def __init__(self):
        self.left_room = False
        self.right_room = False

    def room_5(self):
        pygame.mixer.Channel(4).play(Sounds.door_closing(self))
        print("You enter into a room with nothing in it but two doors and a piano in the corner of the room")
        time.sleep(5)
        response = input("Do you go to the (Piano) or to the (Doors): ")
        while response.lower() != 'piano' and response.lower() != 'doors':
            response = input("Please enter Piano or Doors: ")
        if response.lower() == 'piano':
            response = input("Do you (Inspect) the piano, (Play) the piano or go to the (Doors): ")
            while response.lower() != 'inspect' and response.lower() != 'play' and response.lower() != 'doors':
                response = input("Please enter Inspect, Play or Doors: ")
            if response.lower() == 'inspect':
                print("You look at the piano and notice through the top of it that all the strings are broken: ")
                time.sleep(5)
                repsonse = ("Do you (Play) the piano or go to the (Doors): ")
                while response.lower() != 'play' and response.lower() != 'doors':
                    response = input("Please enter either Play or Doors: ")
            if response.lower() == 'play':
                print("You sit down and try to play the piano but it makes no sound")
                time.sleep(5)
                response = input("Do you go to the (Doors): ")
                while response.lower() != 'doors':
                    response = input("Please enter Doors: ")
        if response.lower() == 'doors':
            while response.lower() == 'doors':
                print("You walk over to the corner of the room where both doors are.")
                time.sleep(5)
                print("The door on your left is the one directly across from where you came in from.")
                time.sleep(5)
                print("The door on your right is the one directly across from the piano")
                time.sleep(5)
                response = input("Do you go to the (Left) door or the (Right) door: ")
                while response.lower() != 'left' and response.lower() != 'right':
                    response = input("Please enter either Left or Right: ")
                if response.lower() == 'left':
                    print("You walk over to the left door")
                    time.sleep(5)
                    response = input("Do you (Inspect) the door, (Open) "
                                     "the door, or go (Back) to the middle of the room: ")
                    while response.lower() != 'inspect' and response.lower() != 'open' and response.lower() != 'right':
                        response = input("Please enter Inspect, Open, or Back: ")
                    if response.lower() == 'inspect':
                        print("You look at the door and notice nothing of importance to it.")
                        time.sleep(5)
                        response = input("Do you (Open) the door or go (Back) to the middle of the room: ")
                        while response.lower() != 'open':
                            response = input("Please enter Open or Other: ")
                    if response.lower() == 'open':
                        self.left_room = True
                        pygame.mixer.Channel(5).play(Sounds.door_squeak(self))
                        print("You open the door and continue into the next room")
                        time.sleep(5)
                    if response.lower() == 'back':
                        response = 'doors'
                if response.lower() == 'right':
                    print('You walk over to the door on the right hand side')
                    time.sleep(5)
                    response = input("Do you (Inspect) the door, (Open) "
                                     "the door or go (Back) to the middle of the room: ")
                    while response.lower() != 'inspect' and response.lower() != 'open' and response.lower() != 'back':
                        response = input("Please enter either Inspect, Open, or Back")
                    if response.lower() == 'inspect':
                        print("You look at the top of the door and see a spider sprawled across it")
                        time.sleep(5)
                        response = input("Do you (Open) the door or go (Back) to the middle of the room: ")
                        while response.lower() != 'open' and response.lower() != 'back':
                            response = input("Please enter either Open or Back: ")
                    if response.lower() == 'open':
                        self.right_room = True
                        print("You open the door and continue into the next room")
                        pygame.mixer.Channel(5).play(Sounds.door_squeak(self))
                        time.sleep(5)
                    if response.lower() == 'back':
                        response = 'doors'


    def left_room_checker(self):
        return self.left_room

    def right_room_checker(self):
        return self.right_room
