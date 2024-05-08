import random
from queue import Queue


class FlappyBirdLogic:
    pipe_width = 80
    pipe_hole_size = 240
    pipe_interval = 400
    bird_radius = 40
    speed_horizontal = 400
    jump_acceleration = 600
    jump = False
    gravity = 2000
    bird_x_pos = 200

    def __init__(self):
        self.height = 300
        self.speed_vertical = 0
        self.pipes_tuple = tuple()
        for i in range(380, 1300, self.pipe_interval):
            self.add_pipe(i)

    def add_pipe(self, x: float = 1280):
        self.pipes_tuple += ((x, random.uniform(100, 380)), )

    def update(self, dt: float):
        # Move pipes
        dx = dt * self.speed_horizontal
        self.pipes_tuple = tuple((i - dx, j) for i, j in self.pipes_tuple)
        # Check jump
        if self.jump:
            self.speed_vertical = self.jump_acceleration
            self.jump = False
        # Move bird
        self.height -= dt * self.speed_vertical
        self.speed_vertical -= dt * self.gravity
        # Check collision

        # Check pipe out of bounds
        for i, (x, _) in enumerate(self.pipes_tuple):
            if x < - self.pipe_width:
                ans = list(self.pipes_tuple)
                ans.pop(i)
                ans.append((1280, random.uniform(100, 380)))
                self.pipes_tuple = tuple(ans)
        return 1






