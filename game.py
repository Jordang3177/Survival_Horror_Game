from room_1 import Room1 as Room_1

class Game:
    def play_game(self):
        Room_1.game(self)

if __name__ == '__main__':
    game = Game()
    game.play_game()