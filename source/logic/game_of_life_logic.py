import os
import random


class GameOfLifeLogic:
    def __init__(self, width: int = 64, height: int = 32, map_type: str = ""):  # height was 36
        self.width = width
        self.height = height
        self.live_cells = 0
        self.map = self.get_map_func(map_type)()
        self.map_old = []

    def zeros_map(self):
        return [[0 for i in range(self.width)] for j in range(self.height)]

    def random_map_bad(self):
        ans = self.zeros_map()
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                ans[y][x] = random.choice((0, 1))
        return ans

    def import_map(self, file_name: str = "gosper-glider-gun.txt"):
        os.chdir(r"../data")
        ans = [[0 for _ in range(self.width)]]
        with open(file_name) as my_file:
            for y, line in enumerate(my_file):
                if y > self.height:
                    break
                row = list([0])
                for x, char in enumerate(line):
                    if x > self.width:
                        break
                    if 'X' == char:
                        row.append(1)
                    else:
                        row.append(0)
                ans.append(row)
        print(ans, len(ans), len(ans[0]), sep="\n")
        return ans

    def get_map_func(self, name: str):
        func_map = {"zeros": self.zeros_map,
                    "random": self.random_map,
                    "import": self.import_map}
        try:
            return func_map[name.lower()]
        except KeyError:
            return self.random_map

    def random_map(self):
        return [[0 if y in (0, self.height - 1) or x in (0, self.width - 1) else random.choice((0, 1))
                for x in range(self.width)] for y in range(self.height)]

    def live_neighbours(self, x: int, y: int) -> int:
        """Returns how many live neighbours a cell has"""
        m = self.map_old
        return m[y-1][x-1] + m[y-1][x] + m[y-1][x+1] + m[y][x-1] + m[y][x+1] + m[y+1][x-1] + m[y+1][x] + m[y+1][x+1]

    def update(self):
        self.map_old = self.map
        self.map = self.zeros_map()
        live_cells = 0

        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                live_neighbours = self.live_neighbours(x, y)
                if not self.map_old[y][x]:
                    if 3 == live_neighbours:
                        self.map[y][x] = 1
                        live_cells += 1
                else:
                    if (2 == live_neighbours) or (3 == live_neighbours):
                        self.map[y][x] = 1
                        live_cells += 1
        self.live_cells = live_cells




"""

    def update(self):
        for y0, y1, y2 in zip(self.map[:-2], self.map[1:-1], self.map[2:]):
            for a, b, c, d, e, f, g, h, i in zip(y0[:-2], y0[1:-1], y0[2:],
                                                 y1[:-2], y1[1:-1], y1[2:],
                                                 y2[:-2], y2[1:-1], y2[2:]):
                live_neighbours = a + b + c + d + f + g + h + i     # not e
                if not e:
                    if 3 == live_neighbours:
                        e = 1
                else:
                    if (live_neighbours < 2) or live_neighbours > 3:
                        e = 0
                        
                        
                        
                        
"""

