import pygame
import time

class Test:
    def test_sounds(self):
        pygame.mixer.init()
        pygame.mixer.Sound.play(pygame.mixer.Sound('Agony_Scream.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Body_Falling.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Bones.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Door_Closing.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('DoorSqueak.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Evil_Laugh.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Far_Away_Movement.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Glass_Breaking.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Others_Bite.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Others_Breathing.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Others_Laugh.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Others_Moving.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Others_Sound.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Side_Door_Gone.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Metal_Door_Opening.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Footsteps_On_Metal.wav'))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Cutting_Rope.wav'))
        time.sleep(3)

    def mixer(self, file):
        pygame.mixer.music.load(file)
        pygame.mixer.musi()

if __name__ == '__main__':
    T = Test()
    T.test_sounds()