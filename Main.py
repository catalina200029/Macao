from Functions import *
from Level import *

pygame.init()

window = pygame.display.set_mode((1000, 500))
is_playing = True

start_level = Start_Level(window)
#play_level = Play_Level()

current_level = start_level

while is_playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_playing = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        is_playing = False

    current_level.draw()

    pygame.display.update()


finish_program()