import numpy as np
from ..Component import Component
from .TransformComponent import TransformComponent


class MotionComponent(Component):
    __slots__ = ['velocity', 'acceleration', 'gravity', 'mass', '__transform']

    defaults = dict([
        ('velocity', np.zeros(3)),
        ('acceleration', np.zeros(3)),
        ('gravity', np.zeros(3)),
        ('mass', 1)
    ])

    def __init__(self, entity=None, **properties):
        self.__transform = None
        self.velocity = None
        super().__init__(entity, **properties)

    def init(self):
        self.__transform = self.entity.get_component(TransformComponent)

    def update(self, dt=None):
        if self.__transform is not None:
            self.velocity = self.velocity + (self.gravity + self.acceleration) * dt
            self.__transform.position = self.__transform.position + self.velocity * dt
