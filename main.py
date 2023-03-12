import pygame

from Character import Character
from object import Object
from object import ObjectType


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

    def create_objects(self):
        object1 = Object(200, 300, ObjectType.SOLID)
        object2 = Object(50, 440, ObjectType.SOLID)
        return [object1, object2]

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
        self.character.move(self.window.get_width(), self.window.get_height())

    def render(self):
        self.window.fill((51, 51, 51))
        pygame.draw.rect(self.window, (0, 0, 200), (self.character.x, self.character.y, self.character.width, self.character.height))
        self.window.blit(self.character.img, (self.character.x, self.character.y))
        for game_object in self.objects:
            pygame.draw.rect(self.window, (0, 255, 0), (game_object.x, game_object.y, game_object.width, game_object.height))
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
