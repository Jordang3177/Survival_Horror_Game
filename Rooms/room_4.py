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
        self.dead = False

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
            if response.lower() == 'calm':
                print("You look away from the picture to try to calm yourself down")
                time.sleep(3)
                print("You breathe heavily to try to steady yourself, knowing that the only way to save"
                      " yourself and your husband is to remain calm and think rationally")
                time.sleep(10)
                print("After taking a moment to collect yourself, you look around to see that a door has appeared")
                time.sleep(5)
                response = input("Do you want to go to the (Door) or (Stay) and think: ")
                while response.lower() != 'door' and response.lower() != 'stay':
                    response = input("Please enter either Door or Stay: ")
                if response.lower() == 'stay':
                    print("You sit on the floor for a moment to think what the next thing you can do is")
                    time.sleep(3)
                    while response.lower() != 'door':
                        response = input("Do you want to go to the (Door) or (Stay) and continue thinking: ")
                if response.lower() == 'door':
                    print("You walk over to the door and continue on, trying not to think of the horrible things that"
                          " must be happening to your husband")
                    time.sleep(3)
                    pygame.mixer.Channel(2).play(Sounds.door_squeak(self))
                    return
        if response.lower() == 'cry':
            print("You look to the picture of your husband and know the pain that he must be in.")
            time.sleep(7)
            print("You know that there is little you can do. You feel a wave coming over you that is foreign to you")
            time.sleep(7)
            print("You begin to break down and cry, kneeling to the ground, hoping for any repreieve from this moment")
            time.sleep(7)
            print("You begin hoping that this must be some sick nightmarish dream or something else")
            time.sleep(7)
            print("This can't possibly be real can it? You and your husband are nobodies, you wake up at 7am every"
                  " morning for work, come home and make dinner")
            time.sleep(7)
            print("Why would this possibly happen to you. What did you "
                  "do so wrong that made this the reality you live in")
            time.sleep(7)
            print("You wonder if it's even worth it, what's the point you think. Can you really save your husband?")
            time.sleep(7)
            print("And even if you could save him from this man, could you even get out alive?")
            time.sleep(7)
            print("You keep crying, like a waterfall of emotions coming over you, and don't know when you will stop")
            time.sleep(7)
            print("You have no idea what to do next")
            time.sleep(7)
            response = input("Do you (Continue) on or (End) it now: ")
            while response.lower() != 'continue' and response.lower() != 'end':
                response = input("Please enter either Continue or End: ")
            if response.lower() == 'end':
                self.dead = True
                #Sad music plays
                print("You take the picture frame that you are holding in your hand and smash it on the ground")
                time.sleep(7)
                print("You pick up the broken piece of glass on the ground")
                time.sleep(7)
                print("You think of the great memories you and your husband have shared")
                time.sleep(7)
                print("That time you went to Disneyland and just sat down at an ice cream store and watched people go by for hours")
                time.sleep(10)
                print("You hold that memory in your head as you let the glass slide across your arms")
                time.sleep(10)
                print("Thinking about the Chocolate Chip Mint Cone that you got that day")
                time.sleep(10)
                print("About the many laughs you shared")
                time.sleep(10)
                print("You feel the blood running thick onto the floor and feel light headed")
                time.sleep(10)
                print("Thinking about the cool feeling of that ice cream on a hot summer's day")
                time.sleep(10)
                print("The way that your husband and you didn't have "
                      "a care in the world but what was right in front of you")
                time.sleep(10)
                print("You fall to the floor barely conscious")
                time.sleep(10)
                print("Holding on to those happy moments, looking up at the ceiling and saying sorry that you wern't strong enough"
                      " knowing your husband would forgive you.")
                time.sleep(15)
                print("A warmth comes over you and a lightness that feels like you are floating")
                time.sleep(10)
                print("You close your eyes, thinking back to that day, and having that memory as your last")
                time.sleep(15)
                return
            if response.lower() == 'continue':
                print("You know that it will be hard")
                time.sleep(5)
                print("Hell it might even be impossible")
                time.sleep(5)
                print("But you have to continue forward you tell yourself")
                time.sleep(5)
                print("Not for yourself, but for the man you love with all your heart")
                time.sleep(5)
                print("You stand up and wipe off the tears, and look forward to see a door")
                time.sleep(5)
                print("You walk over to the Door and continue onward")
                pygame.mixer.Channel(1).play(Sounds.door_squeak(self))
                time.sleep(5)
                return


    def anger_checker(self):
        return self.anger_break

    def game_over_checker(self):
        return self.dead