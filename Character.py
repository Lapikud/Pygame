import pygame

class Character:
    def __init__(self):
        self.x, self.y = 120, 120
        self.vx, self.vy = 0, 0
        self.speed = 5

    def change_direction(self, key: pygame.constants):
        if key == pygame.K_RIGHT or key == pygame.K_d:
            self.vx = self.speed
        elif key == pygame.K_LEFT or key == pygame.K_a:
            self.vx = -self.speed
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.vy += self.speed
        elif key == pygame.K_UP or key == pygame.K_w:
            self.vy = -self.speed

    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def halt(self):
        self.vx, self.vy = 0, 0