import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))
        self.end_surface = pygame.Surface((640, 480))
        self.end_surface.fill((255, 0, 0))
        self.clock = pygame.time.Clock()
        self.running = True
        self.x, self.y = 120, 120
        self.vx, self.vy = 0, 0
        self.speed = 5

    def event(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.vx = self.speed
                elif event.key == pygame.K_LEFT:
                    self.vx = -self.speed
                elif event.key == pygame.K_DOWN:
                    self.vy += self.speed
                elif event.key == pygame.K_UP:
                    self.vy = -self.speed
            elif event.type == pygame.KEYUP:
                self.vx, self.vy = 0, 0

    def update(self):
        pass

    def render(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.window.fill((51, 51, 51))
        pygame.draw.rect(self.window, (0, 0, 200), (self.x, self.y, 40, 40))
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
