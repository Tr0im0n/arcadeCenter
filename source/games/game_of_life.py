
import pygame
from source.logic.game_of_life_logic import GameOfLifeLogic
from source.surfaces.hue_cycler import HueCyclerSingleton


def gol_env(screen: pygame.Surface, map_type: str = "") -> None:
    gol = GameOfLifeLogic(map_type=map_type)
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

        hue_cycler.update()
        screen.fill(hue_cycler.color)
        gol.update()
        show(screen, gol)
        print(gol.live_cells)
        pygame.display.update()
        clock.tick(15)


def show(screen: pygame.Surface, gol: GameOfLifeLogic) -> None:
    color = (255, 255, 255)
    a = 20
    b = 16
    for y in range(gol.height):
        for x in range(gol.width):
            if gol.map[y][x]:
                pygame.draw.rect(screen, color, (a * x, a * y, b, b))

