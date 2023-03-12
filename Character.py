import pygame

class Character:
    def __init__(self):
        self.x, self.y = 120, 120
        self.vx, self.vy = 0, 0
        self.speed = 5

    def change_direction(self, key: pygame.constants):
        if key == pygame.K_RIGHT:
            self.vx = self.speed
        elif key == pygame.K_LEFT:
            self.vx = -self.speed
        elif key == pygame.K_DOWN:
            self.vy += self.speed
        elif key == pygame.K_UP:
            self.vy = -self.speed

    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def halt(self):
        self.vx, self.vy = 0, 0