import numpy as np
import GameEngine as ge
from glumpy import gloo, gl, glm, app
from ..System import System


class RenderSystem(System):
    """ Sistema de renderizado """
    components = ['DrawComponent', 'WallComponent']

    def __init__(self, name=None, components=[]):
        super(RenderSystem, self).__init__(name, components)
        self.window = None

    def init(self):
        gl.glEnable(gl.GL_DEPTH_TEST)
        for e in self.entities:
            draw = e.draw
            view = np.eye(4, dtype=np.float32)
            glm.translate(view, 0, 0, -20)
            model = np.eye(4, dtype=np.float32)
            projection = np.eye(4, dtype=np.float32)

            p = gloo.Program(ge.vertex_shaders['v1'], ge.fragment_shaders['f1'])
            p['u_view'] = view
            p['u_projection'] = projection
            p['u_model'] = model
            p.bind(draw.vertex_buffer)

            draw.program_shader = p
            if draw.vertex_buffer is None:
                draw.set_vertex(draw.vertex)
            if draw.index_buffer is None:
                draw.set_index(draw['index'])
            if self.window is not None:
                draw.set_projection(self.window.width, self.window.height)
            draw.set_color(draw.color)

    def update(self, dt=None):
        for e in self.entities:
            draw_component = e.draw
            if not draw_component.visible:
                return
            # if 'physics' in e.components:
            #     pos = e.physics.position
            #     draw_component.program_shader['u_model'] = glm.translation(pos[0], pos[1], pos[2])
            transform = e.get_component(ge.TransformComponent)
            if transform is not None:
                draw_component.program_shader['u_model'] = transform.M
            draw_component.program_shader.draw(draw_component.draw_type, draw_component.index_buffer)

    def resize(self, w, h):
        for e in self.entities:
            e.draw.set_projection(w, h)
