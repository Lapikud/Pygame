from enum import Enum


class ObjectType(Enum):
    SOLID = 1
    GATE = 2
    ITEM = 3


class Object:

    def __init__(self, start_x, start_y, object_type):
        self.x, self.y = start_x, start_y
        self.width = 40
        self.height = 40
        self.type = object_type
        self.container = None
        self.destroyed = False

    def add_item(self, item):
        if self.type == ObjectType.ITEM:
            self.container = item

