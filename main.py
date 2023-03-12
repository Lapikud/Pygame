import pygame

from Character import Character
from object import Object
from object import ObjectType
from item import Item
from gate import Gate


class Game:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480
        self.window = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.end_surface = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.end_surface.fill((255, 0, 0))
        self.clock = pygame.time.Clock()
        self.running = True
        self.character = Character()
        self.objects = self.create_objects()
        self.background = pygame.image.load("backgrounds/bg1.png").convert_alpha()

    def create_objects(self):
        object1 = Object(200, 300, ObjectType.SOLID)
        object2 = Object(50, 440, ObjectType.SOLID)
        object_item = Object(500, 400, ObjectType.ITEM)
        object_item.add_item(Item("Sword"))
        gate1 = Gate(pygame.image.load("backgrounds/bg2.png").convert_alpha())
        object_gate1 = Object(600, 120, ObjectType.GATE)
        object_gate1.add_item(gate1)

        return [object1, object2, object_item, object_gate1]

    def event(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                self.character.change_direction(event.key)
            elif event.type == pygame.KEYUP:
                self.character.release_key(event.key)

    def update(self):
        for game_object in self.objects:
            collision = self.character.detect_collision(game_object)
            if game_object.type == ObjectType.SOLID and \
                    (collision["vertical"] and collision["horizontal"]):
                print("Collision with object at ", game_object.x, game_object.y)
                print(collision)
            if game_object.type == ObjectType.ITEM and \
                    (collision["vertical"] and collision["horizontal"]):
                print("collect object")
                self.character.add_item(game_object.container)
                game_object.destroyed = True
            if game_object.type == ObjectType.GATE and \
                    (collision["vertical"] and collision["horizontal"]):
                print("move to another room")
                gate = game_object.container
                self.background = gate.background
                self.objects = gate.objects
                self.character.move_to_position(game_object.x - 600, game_object.y)
                break
        self.character.move(self.window.get_width(), self.window.get_height())
        self.objects = [x for x in self.objects if not x.destroyed]

    def render(self):
        self.window.fill((51, 51, 51))
        self.window.blit(self.background, (0, 0))
        pygame.draw.rect(self.window, (0, 0, 200),
                         (self.character.x, self.character.y, self.character.width, self.character.height))
        self.window.blit(self.character.img, (self.character.x, self.character.y))
        for game_object in self.objects:
            pygame.draw.rect(self.window, (0, 255, 0),
                             (game_object.x, game_object.y, game_object.width, game_object.height))
        pygame.display.update()

    def run(self):
        while self.running:
            self.event()
            self.update()
            self.render()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
