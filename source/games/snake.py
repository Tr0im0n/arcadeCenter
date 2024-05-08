import pygame

from source.logic.snake_logic import SnakeLogic
from source.surfaces.hue_cycler import HueCyclerSingleton


def snake_env(screen: pygame.Surface):
    snake = SnakeLogic()
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

        do_arrows(snake)

        hue_cycler.update()
        screen.fill(hue_cycler.color)
        if not snake.update():
            high_score = snake.length
            print(high_score)
            snake = SnakeLogic()
        show(screen, snake)
        pygame.display.update()
        clock.tick(10)


def do_arrows(snake):
    pk = pygame.key.get_pressed()
    if (pk[pygame.K_w] or pk[pygame.K_UP]) and "down" != snake.direction:
        snake.direction = "up"
    elif (pk[pygame.K_a] or pk[pygame.K_LEFT]) and "right" != snake.direction:
        snake.direction = "left"
    elif (pk[pygame.K_s] or pk[pygame.K_DOWN]) and "up" != snake.direction:
        snake.direction = "down"
    elif (pk[pygame.K_d] or pk[pygame.K_RIGHT]) and "left" != snake.direction:
        snake.direction = "right"
    elif pk[pygame.K_SPACE]:
        snake.direction = "space"


def show(screen: pygame.Surface, snake: SnakeLogic) -> None:
    white = (255, 255, 255)
    black = (0, 0, 0)
    a = 20
    b = 16
    for y in range(snake.height):
        for x in range(snake.width):
            if snake.map[y][x]:
                pygame.draw.rect(screen, white, (a * x, a * y, b, b))
    pygame.draw.rect(screen, black, (snake.width * a, 0, a, snake.height * a))
    pygame.draw.rect(screen, black, (0, snake.height * a, snake.width * a, a))
