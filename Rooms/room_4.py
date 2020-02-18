import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from Sound_Files.sounds import _Sounds as Sounds
from Rooms.room_2 import Room2 as Room_2

class Room4:
    def __init__(self):
        self.anger_break = False
        self.insanity = Room_2.insanity_counter(self)

    def room_4(self):
        pygame.mixer.Channel(1).play(Sounds.door_closing(self))
        time.sleep(1)
        print("You come into a room and see a picture of someone you love on a pedastal")
        response = input("(Go) to the pedestal: ")
        time.sleep(3)
        print("You can't stop yourself from going to the picture")
        time.sleep(3)
        print("You walk over and as soon as you get close you hear something behind you falling")
        time.sleep(3)
        pygame.mixer.Channel(1).play(Sounds.side_door_gone(self))
        print("You turn around to notice that the door behind you is gone")
        time.sleep(3)
        print("After looking around some more you realize that this room has nothing in it but "
              "the pedestal with the picture on it")
        time.sleep(3)
        print("You hear the rushing of footsteps behind you")
        #Add movement sounds
        time.sleep(3)
        print("You look down to the picture and see your husband in a chair with a gag on him")
        time.sleep(3)
        print("The sound of speakers comes back")
        time.sleep(3)
        print("There is a long pause before a voice starts")
        time.sleep(10)
        print("the voice says \" Please do make haste, for I have a lot of plans that I hope you will soon be apart of"
              " oh, and your husband says hi")
        time.sleep(3)
        pygame.mixer.Channel(2).play(Sounds.evil_laugh(self))
        print("\" We are all ready for you and please mind my pet, he is rather...")
        time.sleep(3)
        print("skittish")
        time.sleep(3)
        pygame.mixer.Channel(3).play(Sounds.evil_laugh(self))
        print("The sounds cut out and you only have the picture in your hand")
        time.sleep(3)
        response = input("Do you (Scream) out at the man, or (Cry) for the pain of what might happen to your husband: ")
        while response.lower() != 'scream' and response.lower() != 'cry':
            response = input("Please enter either Scream or Cry: ")
        if response.lower() == 'scream':
            print('You scream and yell at nothing but the air around you filled with rage')
            time.sleep(3)
            print("in your fit of rage you throw the picture and hear the crack of glass as the picture frame is broken")
            #Add glass breaking sound
            time.sleep(3)
            #Add Others Breathing sound
            print("Your rage seemed to have brought some other manifestation of evil towards you")
            response = input("Do you keep getting (Angry) or (Calm) down: ")
            while response.lower() != 'angry' and response.lower() != 'calm':
                response = input("Please enter either Angry or Calm: ")
            if response.lower() == 'angry':
                self.insanity += 1
                print("You get angrier and angrier not knowing what limit you "
                      "may have but not stopping to think about it")
                time.sleep(3)
                print("You feel a sudden chill run up your spine but ignore it in your seething rage")
                time.sleep(3)
                response = input("Do you keep getting (Angry) or (Calm) down: ")
                while response.lower() != 'angry' and response.lower() != 'calm:':
                    response = input('Please enter Angry or Calm: ')
                if response.lower() == 'angry':
                    self.anger_break = True
                    print("You get so mad that you can't seem to control yourself and start screaming louder and louder")
                    time.sleep(3)
                    print("You look up at the speakers and scream")
                    print("IF")
                    time.sleep(1)
                    print("YOU")
                    time.sleep(1)
                    print("HURT")
                    time.sleep(1)
                    print("HIM")
                    time.sleep(1)
                    print("I")
                    time.sleep(1)
                    print("WILL")
                    time.sleep(1)
                    print("KILL")
                    time.sleep(1)
                    print("YOuu...")
                    time.sleep(5)
                    print("While screaming something seems to have taken ahold of you and you no longer can move or speak")
                    time.sleep(3)
                    print("You are only able to look forward and only see "
                          "a pair of red eyes with a sinister grin staring back at you")
                    #Add sounds of Others Breathing
                    print("The speakers sound up again")
                    time.sleep(3)
                    print("\"There is nothing to worry about child. Thank you for your anger and I hope we use it well"
                          " in the war to come\"")
                    time.sleep(5)
                    print("The hold over you breaks but you feel closer to death than you ever have in "
                          "your life and collapse to the floor")
                    #Add sound of falling over
                    time.sleep(5)
                    return


    def anger_checker(self):
        return self.anger_break

