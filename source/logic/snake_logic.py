import random


class SnakeLogic:
    directions = {"left": (-1, 0),
                  "right": (1, 0),
                  "down": (0, 1),
                  "up": (0, -1),
                  "space": (0, 0)}

    def __init__(self, direction: str = "right", width: int = 32, height: int = 18):
        self.direction = direction if direction in self.directions else "right"
        self.width = width
        self.height = height
        self.area = width * height
        self.head = [16, 9]
        self.length = 2
        self.map = self.new_map()
        self.add_fruit()

    def new_map(self):
        ans = [[0 for x in range(self.width)] for y in range(self.height)]
        self.head = [16, 9]
        self.length = 2
        ans[self.head[1]][self.head[0]] = self.length
        return ans

    def add_fruit(self):
        index = random.randrange(0, self.area - self.length, 1)
        for y in range(self.height):
            for x in range(self.width):
                if not 0 == self.map[y][x]:
                    continue
                if index > 0:
                    index -= 1
                else:
                    self.map[y][x] = -1
                    return

    def decrease_tail(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] > 0:
                    self.map[y][x] -= 1

    def update(self):
        if "space" == self.direction:
            return self.length
        # Get new head position
        dx, dy = self.directions[self.direction]
        self.head[0] += dx
        self.head[1] += dy
        # Check for hitting the walls
        if (self.head[0] < 0) or (self.head[0] >= self.width) or (self.head[1] < 0) or (self.head[1] >= self.height):
            return 0
        # Check for hitting your own tail
        if self.map[self.head[1]][self.head[0]] > 0:
            return 0
        # Check for fruit
        if -1 == self.map[self.head[1]][self.head[0]]:
            self.length += 1
            self.add_fruit()
        # Move the tail
        else:
            self.decrease_tail()
        # Placing the head
        self.map[self.head[1]][self.head[0]] = self.length

        return self.length

