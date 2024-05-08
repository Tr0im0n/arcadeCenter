import pygame

width, height = 1280, 720


class ExitMessage(pygame.sprite.Group):     # Group
    def __init__(self):
        super().__init__()

        self.width, self.height = 280, 160

    def update(self):
        pass


def draw_exit_menu(screen, mx=0, my=0):
    menu_width, menu_height = 280, 160
    menu_center_x, menu_center_y = 640, 360
    menu_edge_width = 6
    menu_border_radius = 20
    multiply_color = (127, 127, 127)
    menu_color = (31, 31, 31)

    surf1 = pygame.Surface((menu_width-(2*menu_edge_width), menu_height-(2*menu_edge_width)))
    surf1.fill(multiply_color)
    screen.blit(surf1, (menu_center_x-(menu_width/2)+menu_edge_width, menu_center_y-(menu_height/2)+menu_edge_width),
                special_flags=pygame.BLEND_MULT)

    pygame.draw.rect(screen, menu_color,
                     (menu_center_x-(menu_width/2), menu_center_y-(menu_height/2), menu_width, menu_height),
                     width=menu_edge_width, border_radius=menu_border_radius)



