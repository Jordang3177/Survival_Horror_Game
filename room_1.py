import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class Room1:
    def game(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Shadowlands 5 - Antechamber.mp3")
        pygame.mixer.music.play()
        print("Welcome to the Adventure of a Lifetime")
        response = input("If you are ready to play put (Play), if not then say (Help) : ")
        if response == "Help" or response == 'help':
            print("This game is a text based story based game that will ask you for you input into what to do and where to go. \n"
                  "The Game will tell you what you can input at each time based on parenthesis in the sentence.\n"
                  "For example if you see (Forward) then if you type Forward that is a valid Command.\n"
                  "There are secret commands that won't be found in the text as obvious as others so look carefully. \n"
                  "Please pay attention and remember to Enjoy!")
            time.sleep(5)
        while response != 'Play' and response != 'play' and response != ' play' and response != ' Play':
            response = input("Please enter a valid command of (Play): ")
        print("You wake up in a small dark room not remembering how you got here but there is a sharp pain in your head")
        time.sleep(5)
        print("Before you even begin to orient yourself to the surroundings you hear a large speaker start to turn on and a voice saying ")
        time.sleep(5)
        print("LISTEN FOR I HAVE ONLY TO SAY THIS ONCE. I HAVE CAPTURED YOU AND WANT YOU TO TEST MY FACILITIES. YOU CAN DIE SO BE PREPARED AT EVERY TURN STRANGER!")
        time.sleep(5)
        print("You think you recognize the voice but don't have the time to think about that for now")
        time.sleep(3)
        print("The lights turn on and blind you for a moment. After your eyes adjust you see a chest in front of you.")
        time.sleep(3)
        response = input("Do you (Open) the chest or walk to the (Door): ")
        while response != 'Open' and response != 'open' and response != 'Door' and response != 'door':
            response = input("Please enter a valid command of Open or Door: ")
        if response == "Open" or response == 'open' or response == ' open' or response == ' Open':
            room_1_weapon = True
            print("You open the chest and see a small club inside. You take it out and strap it to your belt")
            response = input("You have opened the chest and found a weapon. There is only the (Door) in front you: ")
        while response != 'Door' and response != 'door':
            response = input("Please enter a valid command of Door: ")
        print("Work in progress, Thank you for playing so far!")