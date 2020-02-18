from Rooms.room_1 import Room1 as Room_1
from Rooms.room_2 import Room2 as Room_2
from Rooms.room_2_side_room import SideRoom as Side_Room
from Rooms.room_3 import Room3 as Room_3
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class Game:
    def play_game(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Sound_Files/Antechamber.wav')
        pygame.mixer.music.play(1000)
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





if __name__ == '__main__':
    game = Game()
    game.play_game()