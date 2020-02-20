from Rooms.room_1 import Room1 as Room_1
from Rooms.room_2 import Room2 as Room_2
from Rooms.room_2_side_room import SideRoom as Side_Room
from Rooms.room_3 import Room3 as Room_3
from Rooms.room_4 import Room4 as Room_4
from Rooms.room_5 import Room5 as Room_5
from Rooms.torture_room import TortureRoom as Torture_Room
import os
import sys

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class Game:
    def play_game(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Sound_Files/Antechamber.wav')
        pygame.mixer.music.play(-1)
        Room_1.__init__(self)
        Room_1.room_1(self)
        weapon = Room_1.weapon_checker(self)
        Room_2.__init__(self)
        Room_2.hallway_1(self)
        side_room = Room_2.side_room_checker(self)
        if side_room:
            Side_Room.storage(self)
            Room_2.hallway_1_return(self)
        insanity = Room_2.insanity_counter(self)
        attacked = Room_2.monster_attacked_checker(self)
        Room_3.__init__(self)
        Room_3.room_3(self)
        Room_4.__init__(self)
        Room_4.room_4(self)
        insanity = Room_4.insanity_counter(self)
        if Room_4.game_over_checker(self):
            return
        if Room_4.anger_checker(self):
            #Add different music to show a different feeling to what is happening now
            Torture_Room.__init__(self)
            Torture_Room.torture_room_anger(self)
            insanity = Torture_Room.insanity_counter(self)
            if Torture_Room.comply_checker(self):
                Torture_Room.tortue_room_anger_comply(self)
                #After this will go into small hallway with two doors
            else:
                Torture_Room.torture_room_anger_fight(self)
                #After this will go into small hallway with two doors
        else:
            Room_5.__init__(self)
            Room_5.room_5(self)
            if Room_5.left_room_checker(self):
                print("Work in Progress")
            if Room_5.right_room_checker(self):
                print("Work in Progress")






if __name__ == '__main__':
    game = Game()
    game.play_game()