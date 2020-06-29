import numpy as np
from glumpy import glm
from ..Component import Component


class TransformComponent(Component):
    defaults = dict([
        ('position', np.zeros(3, dtype=np.float32)),
        ('rotation', np.zeros(3, dtype=np.float32)),
        ('scale', np.ones(3, dtype=np.float32))
    ])

    @property
    def M(self):
        p, r, s = self.position, self.rotation, self.scale
        M = glm.translation(p[0], p[1], p[2])
        glm.scale(M, s[0], s[1], s[2])
        glm.xrotate(M, r[0])
        glm.yrotate(M, r[1])
        glm.zrotate(M, r[2])
        return M
