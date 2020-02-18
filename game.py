from room_1 import Room1 as Room_1
import pygame


class Game:
    def play_game(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Shadowlands-5-Antechamber.wav')
        pygame.mixer.music.play()
        Room_1.start(self)
        room_1 = Room_1()
        weapon = room_1.room_1_weapon

if __name__ == '__main__':
    game = Game()
    game.play_game()