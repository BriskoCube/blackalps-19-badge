import random

import math


class App():
    GRID_POS_CIRCLE = [
        [[43, 11], [64, 11], [85, 11]],
        [[43, 32], [64, 32], [85, 32]],
        [[43, 53], [64, 53], [85, 53]],
    ]

    GRID_POS_CROSS = [
        [[38, 6], [59, 6], [80, 6]],
        [[38, 27], [59, 27], [80, 27]],
        [[38, 48], [59, 48], [80, 48]],
    ]

    def __init__(self, badge):
        self.badge = badge
        self.NAME = "Tictactoe"

    def run(self):
        self.grid = [[None, None, None], [None, None, None], [None, None, None]]

        self.is_cross = True
        self.cursorY = 1
        self.cursorX = 1
        self.enterCount = 0

        self.draw_grid()

        self.draw_cursor(self.GRID_POS_CROSS[1][1][0],
                         self.GRID_POS_CROSS[1][1][1])

        self.badge.screen.oled.show()

        while True:
            key = self.badge.buttons.wait_button()

            self.draw_cursor(self.GRID_POS_CROSS[self.cursorY][self.cursorX][0],
                             self.GRID_POS_CROSS[self.cursorY][self.cursorX][1], 0)

            if key == 'DOWN':
                self.cursorY = 2 if self.cursorY > 1 else self.cursorY + 1
            if key == 'UP':
                self.cursorY = 0 if self.cursorY < 1 else self.cursorY - 1
            if key == 'LEFT':
                self.cursorX = 0 if self.cursorX < 1 else self.cursorX - 1
            if key == 'RIGHT':
                self.cursorX = 2 if self.cursorX > 1 else self.cursorX + 1
            if key == 'ENTER':
                if self.grid[self.cursorY][self.cursorX] is None:
                    if self.is_cross:
                        self.draw_cross(self.GRID_POS_CROSS[self.cursorY][self.cursorX][0],
                                        self.GRID_POS_CROSS[self.cursorY][self.cursorX][1], 11)
                    else:
                        self.draw_circle(self.GRID_POS_CIRCLE[self.cursorY][self.cursorX][0],
                                         self.GRID_POS_CIRCLE[self.cursorY][self.cursorX][1], 6)

                    self.grid[self.cursorY][self.cursorX] = self.is_cross
                    self.is_cross = not self.is_cross
                self.enterCount += 1
            else:
                self.enterCount = 0

            self.draw_cursor(self.GRID_POS_CROSS[self.cursorY][self.cursorX][0],
                             self.GRID_POS_CROSS[self.cursorY][self.cursorX][1])

            # self.badge.screen.oled.pixel(int(snake[0][1]), int(snake[0][0]), 1)

            i = 0

            self.badge.screen.oled.show()

            if self.enterCount > 3:
                return

    def draw_grid(self):
        self.badge.screen.oled.fill(0)
        self.badge.screen.oled.rect(32, 0, 63, 63, 1)

        self.badge.screen.oled.hline(32, 21, 63, 1)
        self.badge.screen.oled.hline(32, 42, 63, 1)

        self.badge.screen.oled.vline(53, 0, 63, 1)
        self.badge.screen.oled.vline(74, 0, 63, 1)

    def draw_circle(self, cx, cy, r):
        for i in range(360):
            x = cx + int(r * math.cos(math.radians(i)))
            y = cy + int(r * math.sin(math.radians(i)))
            self.badge.screen.oled.pixel(x, y, 1)

    def draw_cross(self, x, y, size):
        for i in range(size):
            self.badge.screen.oled.pixel(x + i, y + i, 1)
            self.badge.screen.oled.pixel(x + i, y + size - i - 1, 1)

    def draw_cursor(self, x, y, v=1):
        self.badge.screen.oled.rect(x - 3, y - 3, 15, 15, v)

    '''def draw_circle(self):
        self.badge.screen.oled.c
'''
