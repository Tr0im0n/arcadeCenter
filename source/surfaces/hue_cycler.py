import pygame


class HueCyclerSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, hue: float = 0, hue_step: float = 0.2):
        if hasattr(self, '_hue'):
            return
        self._hue = hue
        self._hue_step = hue_step
        self._color = pygame.Color(0, 0, 0)  # Black

    def update(self):
        self._hue += self._hue_step
        if self._hue > 360:  # Hue has a range of (0, 360)
            self._hue = 0
        self._color.hsva = (self._hue, 100, 100, 100)

    @property
    def color(self):
        return self._color


"""
class HueCycler:
    def __init__(self, hue: float = 0, hue_step: float = 0.2):
        self.hue = hue
        self.hue_step = hue_step
        self.color = pygame.Color(0, 0, 0)  # Black

    def update(self):
        self.hue += self.hue_step
        if self.hue > 360:  # Hue has a range of (0, 360)
            self.hue = 0
        self.color.hsva = (self.hue, 100, 100, 100)


class HueCyclerNoInstance:
    hue = 0
    hue_step = 0.2
    color = pygame.Color(0, 0, 0)  # Black

    def __new__(cls, *args, **kwargs):
        raise TypeError("This class cannot be instantiated.")

    @staticmethod
    def update():
        cls = HueCyclerNoInstance
        cls.hue += cls.hue_step
        if cls.hue > 360:  # Hue has a range of (0, 360)
            cls.hue = 0
        cls.color.hsva = (cls.hue, 100, 100, 100)

"""
