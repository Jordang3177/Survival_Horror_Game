from Sound_Files.sounds import _Sounds as Sounds
import time
import os
from Rooms.room_1 import Room1 as Room_1
from Rooms.room_2_side_room import SideRoom as Side_Room
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class Room2:
    def __init__(self):
        self.side_room = False
        self.went_to_side_door = False
        self.monster_attacked = False
        self.room_2_secret = False
        self.insanity = 0

    def hallway_1(self):
        pygame.mixer.Channel(1).play(Sounds.door_closing(self))
        print("You hear the door close behind you")
        time.sleep(2)
        print("Looking forward you see a small hallway with a door at the end of the hallway"
              " and a door on the side in between where you are and where the end of the hallway is")
        time.sleep(5)
        response = input("Go to the (Main) Door or the (Side) Door: ")
        while response.lower() != 'main' and response .lower() != 'side':
            response = input("Please enter either (Main) or (Side): ")
        if response.lower() == 'side':
            self.went_to_side_door = True
            print("You walk up to the Side door")
            time.sleep(3)
            response = input("Do you (Inspect) the door or (Open) it: ")
            while response.lower() != 'inspect' and response.lower() != 'open':
                response = input("Please enter Inspect or Open: ")
            if response.lower() == 'inspect':
                print("You see on the door near the top there is a streak of blood and claw marks near the door knob")
                time.sleep(3)
                pygame.mixer.Channel(1).play(Sounds.others_sound(self))
                print("Behind you, from the door you entered from you hear the same sound as before, getting louder")
                time.sleep(3)
                response = input("Do you (Open) the side door or (Go) to the main door: ")
                while response.lower() != 'open' and response.lower() != 'Go':
                    response = input("Please enter either Open or Go: ")
            if response.lower() == 'open':
                self.side_room = True
                pygame.mixer.Channel(2).play(Sounds.door_squeak(self))
                print("The Door squeaks open before you")
                time.sleep(2)
                pygame.mixer.Channel(3).play(Sounds.evil_laugh(self))
                time.sleep(1)
                print("You hear the sound of someone laughing and the crack of bone while "
                      "someone screams in agony on the speakers")
                time.sleep(2)
                pygame.mixer.Channel(4).play(Sounds.bones(self))
                time.sleep(1)
                pygame.mixer.Channel(5).play(Sounds.agony_scream(self))
                time.sleep(3)
                return
        print("You get to the Main door of the hall")
        time.sleep(3)
        response = input("Do you want to (Inspect) the door or (Open) it: ")
        while response.lower() != 'inspect' and response.lower() != 'open':
            response = input("Please enter either Inspect or Open: ")
        if response.lower() == 'inspect':
            print("There is nothing remarkable about this door. It seems to be just an ordinary wooden door")
            response = input("(Open) the main door: ")
            while response.lower() != 'open':
                response = input("Please enter Open")
        if response.lower() == 'open':
            pygame.mixer.Channel(1).play(Sounds.door_squeak(self))
            print("You continue forward into the next room")
            time.sleep(3)
            return

    def hallway_1_return(self):
        pygame.mixer.Channel(1).play(Sounds.door_closing(self))
        print("You walk away from the side door and start away to the main door in the hallway")
        time.sleep(3)
        pygame.mixer.Channel(2).play(Sounds.side_door_gone(self))
        print("As you walk away from the side door you hear a loud bang and notice "
              "that the side door is no longer there")
        time.sleep(3)
        print("You get to the Main door of the hall")
        time.sleep(3)
        response = input("Do you want to (Inspect) the door or (Open) it: ")
        while response.lower() != 'inspect' and response.lower() != 'open':
            response = input("Please enter either Inspect or Open: ")
        if response.lower() == 'inspect':
            print("There is nothing remarkable about this door. It seems to be just an ordinary wooden door")
            response = input("(Open) the main door: ")
            while response.lower() != 'open':
                response = input("Please enter Open")
        if response.lower() == 'open':
            pygame.mixer.Channel(1).play(Sounds.door_squeak(self))
            print("As you leave the room you see a form out of the corner of your eye")
            time.sleep(3)
            response = input("Do you (Turn) back to see what it was or (Move) forward: ")
            while response.lower() != 'turn' and response.lower() != 'move':
                response = input("Please enter Turn or Move: ")
            if response.lower() == 'turn':
                print("As you turn around there are a set of red eyes staring "
                      "at you from where the side door used to be")
                time.sleep(3)
                response = input("Do you (Go) towards it or (Run): ")
                while response.lower() != 'go' and response.lower() != 'run':
                    response = input("Please enter either Go or Run: ")
                if response.lower() == 'go':
                    weapon = Room_1.weapon_checker(self)
                    if weapon:
                        print("You walk up to the pair of eyes and you start to see a set of massive teeth")
                        time.sleep(3)
                        pygame.mixer.Channel(1).play(Sounds.others_breathing(self))
                        print("You feel it breathing on you and the stench of something rotten")
                        time.sleep(3)
                        response = input("Do you (Attack) it with your weapon or (Run): ")
                        while response.lower() != 'attack' and response.lower() != 'run':
                            response = input("Please enter either Attack or Run: ")
                        if response.lower() == 'attack':
                            self.monster_attacked = True
                            print('You swipe with your club at the pair of eyes and watch as it merely fades'
                                  ' into the shadows laughing all the while')
                            time.sleep(3)
                            pygame.mixer.Channel(2).play(Sounds.others_laugh(self))
                            print("There is nothing in front of you but the wall")
                            time.sleep(3)
                            print("There is a small clink sound near you")
                            time.sleep(3)
                            response = input("Do you (Go) back to the main door or (Inspect) the noise: ")
                            while response.lower() != 'go' and response.lower() != 'inspect':
                                response = input("Please enter Go: ")
                            if response.lower() == 'inspect':
                                self.room_2_secret = True
                                print("You see something that looks like a tooth and pick it up "
                                      "off the ground and put it in your pocket")
                                time.sleep(3)
                                print("There is nothing left to do but go to the door")
                                response = 'go'
                            if response.lower() == 'go':
                                print("As you walk to the door you notice a slightly warmer feeling in the room.")
                                time.sleep(3)
                                print("You open the door and proceed forward")
                                pygame.mixer.Channel(1).play(Sounds.door_squeak(self))
                                time.sleep(3)
                                return
                        if response.lower() == 'run':
                            self.insanity += 1
                            print("You begin to run away from the monster and immediately g"
                                  "o to the door as fast as possible")
                            time.sleep(3)
                            print("You open the door and hear laughter all around you ")
                            pygame.mixer.Channel(2).play(Sounds.door_squeak(self))
                            pygame.mixer.Channel(3).play(Sounds.others_laugh(self))
                            print("You feel a chilling feeling on you as you move forward into the next room")
                            time.sleep(3)
                            return
                    else:
                        print("You walk up to the pair of eyes and you start to see a set of massive teeth")
                        time.sleep(3)
                        pygame.mixer.Channel(4).play(Sounds.others_breathing(self))
                        print("You feel it breathing on you and the stench of something rotten")
                        time.sleep(3)
                        response = input("Do you (Attack) it with your fists or (Run): ")
                        while response.lower() != 'attack' and response.lower() != 'run':
                            response = input("Please enter either Attack or Run: ")
                        if response.lower() == 'attack':
                            self.insanity += 3
                            print("You swipe at the monster with your fists")
                            time.sleep(3)
                            print(
                                "But as your fists get close the teeth come rushing at your arm and clamp down hard")
                            pygame.mixer.Channel(5).play(Sounds.others_bite(self))
                            time.sleep(3)
                            print(
                                "You scream in fear and look at your arm to see the damage, but nothing seems to be"
                                " wrong with it")
                            time.sleep(3)
                            print("You feel a sudden ache in your head and notice that the eyes are gone")
                            time.sleep(3)
                            print("There is nothing to do but go back to the main door and proceed forward")
                            time.sleep(3)
                            print("You open the door and feel scared as you move foward into the next room")
                            pygame.mixer.Channel(3).play(Sounds.door_squeak(self))
                            return
                        if response.lower() == 'run':
                            self.insanity += 1
                            print("You begin to run away from the monster and immediately g"
                                  "o to the door as fast as possible")
                            time.sleep(3)
                            print("You open the door and hear laughter all around you ")
                            pygame.mixer.Channel(2).play(Sounds.door_squeak(self))
                            pygame.mixer.Channel(3).play(Sounds.others_laugh(self))
                            print("You feel a chilling feeling on you as you move forward into the next room")
                            time.sleep(3)
                            return
                if response.lower() == 'run':
                    self.insanity += 1
                    print("You turn back to the door and run through as fast as possible")
                    pygame.mixer.Channel(1).play(Sounds.door_squeak(self))
                    time.sleep(3)
                    return
            if response.lower() == 'move':
                print("You open the door and move forward without regard to what is behind you")
                pygame.mixer.Channel(1).play(Sounds.door_squeak(self))
                pygame.mixer.Channel(2).play(Sounds.others_laugh(self))
                time.sleep(3)
                return

    def side_room_checker(self):
        return self.side_room

    def went_to_side_door_checker(self):
        return self.went_to_side_door

    def monster_attacked_checker(self):
        return self.monster_attacked

    def room_2_secret_checker(self):
        return self.room_2_secret

    def insanity_counter(self):
        return self.insanity