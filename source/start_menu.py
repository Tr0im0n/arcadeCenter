
import pygame
from sys import exit

from source.games.flappy_bird import fb_env
from source.games.game_of_life import gol_env
from source.games.snake import snake_env
from source.surfaces.exit_message import draw_exit_menu
from source.surfaces.hue_cycler import HueCyclerSingleton

# Init ########################################################################
pygame.init()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Welcome to the Arcade Center!")
clock = pygame.time.Clock()
start_time = 0
running = True

# Color cycling
hue_cycler = HueCyclerSingleton(0, 0.2)
show_exit_menu = False

# Timer #########################################################################
timer_2s = pygame.USEREVENT + 1
pygame.time.set_timer(timer_2s, 2000)

# Loop ###########################################################################
while running:

    # user inputs
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if show_exit_menu:
                    running = False
                else:
                    show_exit_menu = not show_exit_menu
                # exit_game()
            if event.key == pygame.K_1:
                gol_env(screen, "random")
            if event.key == pygame.K_2:
                snake_env(screen)
            if event.key == pygame.K_3:
                fb_env(screen)

    hue_cycler.update()
    screen.fill(hue_cycler.color)

    if show_exit_menu:
        draw_exit_menu(screen)

    # end ########################################################################
    pygame.display.update()
    clock.tick(60)


pygame.quit()
