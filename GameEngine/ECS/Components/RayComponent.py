import numpy as np
import GameEngine as ge
from ..Component import Component


class RayComponent(Component):
    defaults = dict([
        ('pos', np.zeros(3)),
        ('dir', np.zeros(3)),
        ('min', 2),
        ('__e', None)
    ])

    def init(self):
        if self['__e'] is None:
            self['__e'] = ge.draw_line(0, 0, 0, 0, (0, 1, 0, 1))

    @staticmethod
    def magnitude(vec):
        return np.sqrt(np.dot(np.array(vec), np.array(vec)))

    @staticmethod
    def norm(vec):
        return np.array(vec) / RayComponent.magnitude(np.array(vec))

    def cast(self, p1, p2):
        pos = np.array(self.pos, dtype=np.float)

        if 'transform' in self.entity.components:
            pos = pos + self.entity.transform.position

        pos = np.array(pos[:2], dtype=np.float)

        direction = np.array(RayComponent.norm(self.dir[:2]), dtype=np.float)
        point1 = np.array(p1[:2], dtype=np.float)
        point2 = np.array(p2[:2], dtype=np.float)
        v1 = pos - point1
        v2 = point2 - point1
        v3 = np.array([-direction[1], direction[0]])
        t1 = np.cross(v2, v1) / np.dot(v2, v3)
        t2 = np.dot(v1, v3) / np.dot(v2, v3)
        if 0.0 <= t1 <= self['min'] and 0.0 <= t2 <= 1.0:
            point = pos + t1 * direction
            test = True
        else:
            point = pos + self['min'] * direction
            test = False
        return test, pos, point, t1

    def update(self, dt=None):
        pass
