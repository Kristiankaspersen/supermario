from abc import ABC, abstractmethod

class Object(ABC):
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Pipe(Object):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height)

class Platform(Object):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height)



