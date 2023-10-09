from abc import ABC, abstractmethod

class Object(ABC):
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_rect(self):
        return self.x, self.y, self.width, self.height
class Pipe(Object):
    def __init__(self):
        self.x = 200
        self.y = 400
        self.width = 50
        self.height = 200
        super().__init__(self.x, self.y, self.width, self.height)


class Platform(Object):
    def __init__(self):
        self.x = 300
        self.y = 300
        self.width = 100
        self.height = 30
        super().__init__(self.x, self.y, self.width, self.height)



