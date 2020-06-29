import numpy as np
from glumpy import gloo, gl, glm
from ..Component import Component


class DrawComponent(Component):
    defaults = dict([
        ('visible', True),
        ('draw_type', gl.GL_LINE_STRIP),
        ('vertex', [[-0.5, -0.5, 0], [0.5, -0.5, 0], [0.5, 0.5, 0], [-0.5, 0.5, 0]]),
        ('index', [0, 1, 2, 3, 0]),
        ('vertex_buffer', None),
        ('index_buffer', None),
        ('color', (1, 1, 1, 1)),
        ('program_shader', None),
    ])

    def set_projection(self, w, h):
        ratio = float(w) / float(h)
        self['program_shader']['u_projection'] = glm.perspective(45.0, ratio, 2.0, 100.0)
        # size = 1.0/w * 12
        # self['program_shader']['u_projection'] = glm.ortho(-w*size, w*size, -h*size, h*size, -100, 100)

    def set_vertex(self, v):
        self['vertex'] = v
        self['vertex_buffer'] = self.__v('a_position', v)
        if self['program_shader'] is not None:
            self['program_shader'].bind(self['vertex_buffer'])

    def set_index(self, i):
        self['index'] = i
        self['index_buffer'] = self.__i(i)

    def set_color(self, c):
        self['color'] = c
        if self['program_shader'] is not None:
            self['program_shader']['u_color'] = c

    @staticmethod
    def __i(index):
        return np.array(index, dtype=np.uint32).view(gloo.IndexBuffer)

    @staticmethod
    def __v(name, vertex):
        V = np.zeros(len(vertex), [(name, np.float32, 3)])
        V[name] = vertex
        return V.view(gloo.VertexBuffer)
