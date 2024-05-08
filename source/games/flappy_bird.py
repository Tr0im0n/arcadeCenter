import pygame

from source.logic.flappy_bird_logic import FlappyBirdLogic
from source.surfaces.hue_cycler import HueCyclerSingleton


def fb_env(screen: pygame.Surface):
    bird = FlappyBirdLogic()
    running = True
    clock = pygame.time.Clock()
    hue_cycler = HueCyclerSingleton()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_SPACE:
                    bird.jump = True

        hue_cycler.update()
        screen.fill(hue_cycler.color)
        if not bird.update(clock.tick(60) / 1000.0):
            high_score = bird.length
            print(high_score)
            snake = FlappyBirdLogic()
        show(screen, bird)
        pygame.display.update()


def show(screen: pygame.Surface, bird: FlappyBirdLogic) -> None:
    white = (255, 255, 255)
    black = (0, 0, 0)

    for x, y in bird.pipes_tuple:
        pygame.draw.rect(screen, black, (x, 0, bird.pipe_width, y))
        pygame.draw.rect(screen, black, (x, y + bird.pipe_hole_size, bird.pipe_width, 720 - y - bird.pipe_hole_size))

    pygame.draw.circle(screen, white, (bird.bird_x_pos, bird.height), bird.bird_radius)




