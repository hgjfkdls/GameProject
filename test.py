import numpy as np
from GameEngine import *

e = Entity('entity_01')
e.transform = TransformComponent()
e.transform.position = np.array([2, 0, 0], dtype=np.float32)
e.transform.rotation = np.array([45, 0, 0], dtype=np.float32)

print(repr(e.get_component(TransformComponent)))
