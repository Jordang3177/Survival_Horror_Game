from room_1 import Room1 as Room_1
from room_2 import Room2 as Room_2
from room_2_side_room import SideRoom as Side_Room
import pygame


class Game:
    def play_game(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Antechamber.wav')
        pygame.mixer.music.play()
        Room_1.__init__(self)
        Room_1.room_1(self)
        weapon = Room_1.weapon_checker(self)
        print(weapon)
        Room_2.__init__(self)
        Room_2.hallway_1(self)
        side_room = Room_2.side_room_checker(self)
        print(side_room)
        if side_room:
            Side_Room.storage(self)


if __name__ == '__main__':
    game = Game()
    game.play_game()