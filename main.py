import pygame

from Character import Character


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))
        self.end_surface = pygame.Surface((640, 480))
        self.end_surface.fill((255, 0, 0))
        self.clock = pygame.time.Clock()
        self.running = True
        self.character = Character()

    def event(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                self.character.change_direction(event.key)
            elif event.type == pygame.KEYUP:
                self.character.halt()

    def update(self):
        pass

    def render(self):
        self.character.move(self.window.get_width(), self.window.get_height())
        self.window.fill((51, 51, 51))
        pygame.draw.rect(self.window, (0, 0, 200), (self.character.x, self.character.y, self.character.width, self.character.height))
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
