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
            self.vy = self.speed
        elif key == pygame.K_UP or key == pygame.K_w:
            self.vy = -self.speed

    def release_key(self, key: pygame.constants):
        if key == pygame.K_RIGHT or key == pygame.K_d:
            self.vx = 0
        elif key == pygame.K_LEFT or key == pygame.K_a:
            self.vx = 0
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.vy = 0
        elif key == pygame.K_UP or key == pygame.K_w:
            self.vy = 0

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

    def detect_collision(self, game_object):
        collisionFrom = {"vertical": None, "horizontal": None}
        if self.x <= game_object.x + game_object.width <= self.x + self.width:
            collisionFrom["horizontal"] = "left"
        if self.y <= game_object.y + game_object.height <= self.y + self.height:
            collisionFrom["vertical"] = "upper"
        if self.x <= game_object.x <= self.x + self.width:
            collisionFrom["horizontal"] = "right"
        if self.y <= game_object.y <= self.y + self.height:
            collisionFrom["vertical"] = "lower"
        return collisionFrom
