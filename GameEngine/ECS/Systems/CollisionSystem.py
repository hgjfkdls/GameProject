import numpy as np
from ..Components import *
from ..System import System


class CollisionSystem(System):
    components = ['RayComponent']

    def init(self):
        for e in self.entities:
            e.ray.init()

    def update(self, dt=None):
        for e in self.entities:
            r = e.ray
            _test = False
            _p1, _p2 = None, None
            _dist = float('inf')
            _wall = None
            for key, w in WallComponent.Catalog.items():
                v = w.vertex_buffer
                i = w.index_buffer
                pos = np.array([0.0, 0.0, 0.0])
                if 'transform' in w.entity.components:
                    pos = w.entity.transform.position
                for t in range(len(i) - 1):
                    test, p1, p2, dist = r.cast(v[i[t]][0] + pos, v[i[t + 1]][0] + pos)
                    if test:
                        _test = True
                        _dist = dist
                        _p1 = p1
                        _p2 = p2
                        _wall = w
                    if dist < _dist and not _test:
                        _p1 = p1
                        _p2 = p2
            line = [(_p1[0], _p1[1], 0), (_p2[0], _p2[1], 0)]
            if _test:
                col = (0, 1, 0, 1)
                if _dist < 0.5:
                    e.transform.position = e.transform.position + np.array((0.0, 0.5 - _dist, 0.0))
                    e.motion.velocity = _wall.entity.motion.velocity
            else:
                col = (1, 0, 0, 1)
            r['__e'].draw.set_color(col)
            r['__e'].draw.set_vertex(line)
