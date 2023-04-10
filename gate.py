
class Gate:

    def __init__(self, background):
        self.background = background
        self.objects = []

    def add_object(self, game_object):
        self.objects.append(game_object)

    def get_object(self):
        if len(self.objects) > 0:
            return self.objects[0]
