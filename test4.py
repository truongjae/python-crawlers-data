import pygame
def auto(f):
    pygame.init()
    pygame.mixer.music.load(f)
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(60)
        pygame.event.poll()
auto("file20.mp3")
auto("file27.mp3")