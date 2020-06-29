import numpy as np
from ..Entity import Entity
from ..Components import *


class Player(Entity):
    def __init__(self, name=None, uid=None):
        super().__init__(name, uid)
        self.transform = TransformComponent()
        self.motion = MotionComponent(gravity=np.array([0.0, -9.8, 0.0], dtype=np.float32))
        self.draw = DrawComponent()
        self.ray = RayComponent(
            pos=np.array([0.0, 0.0, 0.0]),
            dir=np.array([0.0, -1.0, 0.0]),
            min=3.0
        )
