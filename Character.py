import pygame


class Character:
    def __init__(self):
        self.x, self.y = 120, 120
        self.vx, self.vy = 0, 0
        self.speed = 5
        self.width = 40
        self.height = 40
        # import (transparent) sprite and upscale it from 32px to 40 px
        self.img = pygame.image.load("sprites/Dude_Monster.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (40, 40))
        self.inventory = []
        self.direction = {"up": set(), "down": set(), "left": set(), "right": set()}

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
        """
        Checks on every run whether character is located straight above, below or either side of game_object.
        If it is, game_object is added to corresponding side's set in character's variable called self.direction.
        But before adding horizontal value, it is checked whether character WAS already located on vertical tunnel
        (and vice versa) and thus causing collision. If this occurred, the side from where collision was detected
        is returned as a string.
        Also, values are discarded from sets when conditions are not true before collision checks.

        :param game_object: collision subject
        :return: side of character from which collision occurred
        """
        up = self.y >= game_object.y and self.x < game_object.x + game_object.width \
            and self.x + self.width > game_object.x
        down = self.y + self.height <= game_object.y + game_object.height \
            and self.x < game_object.x + game_object.width and self.x + self.width > game_object.x
        left = self.x >= game_object.x and self.y < game_object.y + game_object.height \
            and self.y + self.height > game_object.y
        right = self.x + self.width <= game_object.x + game_object.width \
            and self.y < game_object.y + game_object.height and self.y + self.height > game_object.y

        if not up:
            self.direction["up"].discard(game_object)
        if not down:
            self.direction["down"].discard(game_object)
        if not left:
            self.direction["left"].discard(game_object)
        if not right:
            self.direction["right"].discard(game_object)

        if up:
            if game_object in self.direction["left"]:
                return "left"
            if game_object in self.direction["right"]:
                return "right"
            self.direction["up"].add(game_object)

        if down:
            if game_object in self.direction["left"]:
                return "left"
            if game_object in self.direction["right"]:
                return "right"
            self.direction["down"].add(game_object)

        if left:
            if game_object in self.direction["up"]:
                return "up"
            if game_object in self.direction["down"]:
                return "down"
            self.direction["left"].add(game_object)

        if right:
            if game_object in self.direction["up"]:
                return "up"
            if game_object in self.direction["down"]:
                return "down"
            self.direction["right"].add(game_object)

        return None

    # Inventory methods
    def add_item(self, item):
        self.inventory.append(item)
        print(item.name)

    def delete_item(self, item):
        self.inventory.remove(item)

    def move_to_position(self, move_to_x, move_to_y):
        self.x = move_to_x
        self.y = move_to_y
