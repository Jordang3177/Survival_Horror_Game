import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from Sound_Files.sounds import _Sounds as Sounds
from Rooms.room_4 import Room4 as Room_4

class TortureRoom:
    def __init__(self):
        self.insanity = Room_4.insanity_counter(self)
        self.comply = False

    def torture_room_anger(self):
        time.sleep(5)
        print("You open your eyes slowly. The room you are in is dark with a musty smell")
        time.sleep(5)
        print("You notice that you can't move your arms or legs "
              "anymore, and look down to see that you are tied down to a chair")
        time.sleep(5)
        response = input("Do you (Struggle) or sit (Still): ")
        while response.lower() != 'struggle' and response.lower() != 'still':
            response = input("Please enter either Struggle or Still: ")
        if response.lower() == 'struggle':
            print("You try to struggle out of the chair that you are in for several minutes")
            time.sleep(5)
            print("eventually you feel blood running down your hand "
                  "as you have been moving them and tearing skin trying to break free")
            time.sleep(5)
            print("You stop trying as the pain is becoming too much to bear")
            time.sleep(5)
        if response.lower() == 'still':
            print("You sit still awaiting whatever fate has to offer you")
            time.sleep(5)
        print("You hear a large metal door opening in front of you")
        pygame.mixer.Channel(3).play(Sounds.metal_door_opening(self))
        time.sleep(5)
        print("You hear the sounds of footsteps approaching you")
        pygame.mixer.Channel(4).play(Sounds.footsteps_on_metal(self))
        time.sleep(10)
        print("\" Well, I never would have taken you for the one to let anger take over you so badly")
        time.sleep(5)
        print("but thank you for that, I appreciate you allowing us to use that anger\"")
        time.sleep(5)
        print("A dim light turns on and you see a bloodied table in front of you")
        time.sleep(5)
        print("\" Welcome to my experimentation room! \"")
        time.sleep(5)
        print("You notice a pile of dead bodies all around the room all missing different parts of their bodies, "
              "with blood stains all over")
        time.sleep(10)
        print("You try to see if one of the bodies is your husband, but the light is too dim to see anyone clearly")
        time.sleep(5)
        print("\"Now I'd ask you to sit quietly but we both know that you can't do that \"")
        time.sleep(5)
        print("The man in front of you grabs a knife and cuts your tied hands free")
        pygame.mixer.Channel(5).play(Sounds.cutting_rope(self))
        time.sleep(5)
        response = input("With your hands free do you (Fight) back or (Comply): ")
        while response.lower() != 'fight' and response.lower() != 'comply':
            response = input("Please enter either Fight or Comply: ")
        if response.lower() == 'fight':
            self.insanity += 3
            print("You move your arms slowly as the man wishes you to, "
                  "then as soon as you get close to him you begin to swing at him to punch him")
            time.sleep(7)
            pygame.mixer.Channel(4).play(Sounds.others_moving(self))
            print("Before your hand even gets close to him you feel that same chilling feeling as before")
            time.sleep(5)
            print("You can't move, can't speak, can't breath. You feel total lose of control of your body")
            time.sleep(5)
            print("\"Oh seems you got angry again. Well that's good, "
                  "please don't let go of that. I know my pet loves you all the more for it.\"")
            time.sleep(10)
            pygame.mixer.Channel(4).play(Sounds.others_breathing(self))
            print("\"Now if you wouldn't mind, I'd like to get on with our little experiement\"")
            time.sleep(5)
            print("Without acting your hands move over to the table in front of you")
            time.sleep(5)
            print("The man pulls a rusty machete out from a sheath on his belt")
            time.sleep(5)
            print("Now this may hurt but dont' worry, just know your sacrifice makes it all worth it")
            time.sleep(5)
            print("While watching you try with all your might to be able to fight back against this darkness you feel inside you")
            time.sleep(5)
            print("You see the blade being raise and try harder and harder to just move your hands a little bit")
            time.sleep(5)
            print("You struggle and struggle")
            time.sleep(5)
            #Sound of hand being cut off
            time.sleep(5)
            print("You look at your hand shocked, not understanding what just happened")
            time.sleep(5)
            print("\"Thank you my dear, this hand will be a wonderful means to our end. Now please do sit back down.\"")
            time.sleep(10)
            print("You feel yourself moving back down to the chair, not remember when you stood up")
            time.sleep(5)
            print("You look again at the stump on your arm where your hand used to be, blood flowing easily out of it")
            time.sleep(5)
            print("The man picks up something from the table")
            time.sleep(5)
            print("\"Now I'm not a doctor but we also don't want you to bleed out now do we? So I can only offer you this for now\"")
            time.sleep(10)
            #sounds of flames being put to stump of a hand
            print("You hear the click of something, and then feel an "
                  "intense heat where your arm used to be, a pain so insufferable that you want to scream")
            time.sleep(10)
            print("But nothing comes out of your mouth, and you "
                  "only smell the burning of flesh as your wound becomes cauterized")
            time.sleep(5)
            print("\"Now that the nasty part is done, we can move forward. Come Eltul we have work to do\"")
            time.sleep(5)
            pygame.mixer.Channel(5).play(Sounds.others_moving(self))
            print("You feel control of your body once again, and the darkness inside you is gone.")
            time.sleep(5)
            print("The loss of blood has made you light headed and unable to "
                  "stay awake any longer. You pass out on the chair")
            time.sleep(5)
            return
        if response.lower() == 'comply':
            self.comply = True
            print("You move your arms wherever the man needs them to be and wait patiently for whatever he may do")
            time.sleep(5)
            print("\"No more fighting spirit eh? What happened to wanting to "
                  "kill me? Well no matter, we still need this")
            time.sleep(5)
            print("You close your eyes and slump your head down as if in defeat")
            time.sleep(5)
            #Sounds of hand being cut off
            print("You feel an immense pain and immediately "
                  "look up and start screaming, noticing that your left hand is gone")
            time.sleep(5)
            print("You flail about wildly, knocking yourself and the chair over in a fit of panic and shock")
            time.sleep(5)
            print("\"Now now my dear, we don't need to display such theatrics")
            time.sleep(5)
            print("It's only a hand, surely you don't need both. I left you one \"")
            time.sleep(5)
            print("The man grabs your stump of an arm and takes out something from behind his back")
            time.sleep(5)
            print("You hear a click and then another intense pain, this one followed by a heat you've never felt before")
            #sounds of flame being put to the stump of a hand
            time.sleep(5)
            print("\"Now I'm not a doctor and I'd rather you not die. Yet. So this is all I can offer to you\"")
            time.sleep(10)
            print("\"There all done, now please do get some rest. There is still much to be done. "
                  "Eltul come along now\"")
            time.sleep(5)
            pygame.mixer.Channel(3).play(Sounds.others_laugh(self))
            pygame.mixer.Channel(4).play(Sounds.others_moving(self))
            print("You feel no energy anymore with all that has happened. "
                  "Your eyes feel heavy and you pass out on the cold floor")
            return

    def tortue_room_anger_comply(self):
        print("Work In progress")

    def torture_room_anger_fight(self):
        print("Work In progress")

    def insanity_counter(self):
        return self.insanity

    def comply_checker(self):
        return self.comply