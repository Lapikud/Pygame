import pygame

class Character:
    def __init__(self):
        self.x, self.y = 120, 120
        self.vx, self.vy = 0, 0
        self.speed = 5
        self.width = 40
        self.height = 40

    def change_direction(self, key: pygame.constants):
        if key == pygame.K_RIGHT or key == pygame.K_d:
            self.vx = self.speed
        elif key == pygame.K_LEFT or key == pygame.K_a:
            self.vx = -self.speed
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.vy += self.speed
        elif key == pygame.K_UP or key == pygame.K_w:
            self.vy = -self.speed

    def move(self, screen_width, screen_height):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        if self.x < 0:
            self.x = 0
        if self.x + self.width > screen_width:
            self.x = screen_width - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > screen_height:
            self.y = screen_height - self.height

    def halt(self):
        self.vx, self.vy = 0, 0
