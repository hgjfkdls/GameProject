from ..System import System


class MotionSystem(System):
    components = ['MotionComponent']

    def init(self):
        for e in self.entities:
            e.motion.init()

    def update(self, dt=None):
        for e in self.entities:
            e.motion.update(dt)
