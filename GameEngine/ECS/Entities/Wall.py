from ..Entity import Entity
from ..Components import *


class Wall(Entity):

    def __init__(self, name=None, uid=None):
        super().__init__(name, uid)
        self.__v = []
        self.__i = []
        self.transform = TransformComponent()
        self.motion = MotionComponent()
        self.color = (1, 0, 0, 1)
        self.draw = WallComponent(
            vertex=self.__v,
            vertex_index=self.__i,
            color=self.color
        )

    def set_vertex(self, v):
        self.__v = v
        self.__i = range(len(v))
        self.draw.set_vertex(self.__v)
        self.draw.set_index(self.__i)

    def set_color(self, c):
        self.color = c
        self.draw.set_color(c)
