import os
from .Draw import *
from .ECS import *

vertex_shaders = dict()
fragment_shaders = dict()

for root, dirs, files in os.walk('./GameEngine/vertex_shaders/'):
    for filename in files:
        fn = os.path.splitext(filename)[0]
        vertex_shaders[fn] = open(root + filename, 'r').read()

for root, dirs, files in os.walk('./GameEngine/fragment_shaders/'):
    for filename in files:
        fn = os.path.splitext(filename)[0]
        fragment_shaders[fn] = open(root + filename, 'r').read()
