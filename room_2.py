import time
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class Room2:
    def __init__(self):
        self.side_room = False

    def hallway_1(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Door_Closing.wav'))
        print("You hear the door close behind you")
        time.sleep(2)
        print("Looking forward you see a small hallway with a door at the end of the hallway"
              " and a door on the side in between where you are and where the end of the hallway is")
        time.sleep(5)
        response = input("Go to the (Main) Door or the (Side) Door: ")
        while response.lower() != 'main' and response .lower() != 'side':
            response = input("Please enter either (Main) or (Side): ")
        if response.lower() == 'side':
            print("You walk up to the Side door")
            time.sleep(3)
            response = input("Do you (Inspect) the door or (Open) it): ")
            while response.lower() != 'inspect' and response.lower() != 'open':
                response = input("Please enter Inspect or Open: ")
            if response.lower() == 'inspect':
                print("You see on the door near the top there is a streak of blood and claw marks near the door knob")
                time.sleep(3)
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('Others_Sound.wav'))
                print("Behind you, from the door you entered from you hear the same sound as before, getting louder")
                time.sleep(3)
                response = input("Do you (Open) the side door or (Go) to the main door: ")
                while response.lower() != 'open' and response.lower() != 'Go':
                    response = input("Please enter either Open or Go: ")
            if response.lower() == 'open':
                self.side_room = True
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('DoorSqueak.wav'))
                print("The Door squeaks open before you")
                time.sleep(2)
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('Evil_Laugh.wav'))
                time.sleep(1)
                print("You hear the sound of someone laughing and the crack of bone while "
                      "someone screams in agony on the speakers")
                time.sleep(2)
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('Bones.wav'))
                time.sleep(1)
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('Agony_Scream.wav'))
                time.sleep(3)

    def side_room_checker(self):
        return self.side_room
