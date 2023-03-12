import pygame


class Object:
    def __init__(self, start_x, start_y):
        self.x, self.y = start_x, start_y
        self.width = 40
        self.height = 40