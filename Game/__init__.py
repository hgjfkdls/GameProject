import numpy as np
from glumpy import app
from GameEngine import *

# Variable para el tiempo
t = 0.0

# Creamos los sistemas del juego
motion_system = MotionSystem('physics')
collision_system = CollisionSystem('collision')
render_system = RenderSystem('render')

# Creamos una entidad de tipo Player
player = Player('player')
player.motion.velocity = (1, 10, 0)

# Creamos una entidad de tipo Wall
w = Wall('w001')
w.set_vertex([
    (-10, 1, 0), (-2, 1, 0), (-2, -1, 0), (-1, -2, 0), (1, -2.5, 0),
    (4, -2.5, 0), (6, -2, 0), (7, -1, 0), (7, 1, 0)
])

window = app.Window(width=640, height=480, color=(0.10, 0.10, 0.20, 1.00))
render_system.window = window


@window.event
def on_init():
    System.init_all()


@window.event
def on_draw(dt):
    global t
    window.clear()
    t = t + dt
    w.motion.velocity = np.array((0.0, 10.0 * np.cos(t * 5.0), 0.0), dtype=np.float32)

    System.update_all(dt)


@window.event
def on_resize(width, height):
    render_system.resize(width, height)


# @window.timer(0.5)  # frames per second
# def timer(elapsed):
#     print(app.clock.get_fps())
#
#
# @window.event
# def on_idle(dt):
#     print('Idle event')
#
#
# @window.event
# def on_key_press(symbol, modifiers):
#     print('Key pressed (symbol=%s, modifiers=%s)' % (symbol, modifiers))
#
#
# @window.event
# def on_character(character):
#     print('Character entered (chracter: %s)' % character)
#
#
# @window.event
# def on_key_release(symbol, modifiers):
#     print('Key released (symbol=%s, modifiers=%s)' % (symbol, modifiers))
#
#
# @window.event
# def on_mouse_press(x, y, button):
#     print('Mouse button pressed (x=%.1f, y=%.1f, button=%d)' % (x, y, button))
#
#
# @window.event
# def on_mouse_release(x, y, button):
#     print('Mouse button released (x=%.1f, y=%.1f, button=%d)' % (x, y, button))
#
#
# @window.event
# def on_mouse_motion(x, y, dx, dy):
#     x, y = (x - window.width) / window.width, -(y - window.height) / window.height
#     # mouse.draw.program_shader['a_position'][1] = (x, y, 0)
#
#
# @window.event
# def on_mouse_drag(x, y, dx, dy, button):
#     # print('Mouse drag (x=%.1f, y=%.1f, dx=%.1f, dy=%.1f, button=%d)' % (x, y, dx, dy, button))
#     x, y = (x - window.width) / window.width, -(y - window.height) / window.height
#     # mouse.draw.program_shader['a_position'][1] = (x, y, 0)
#
#
# @window.event
# def on_mouse_scroll(x, y, dx, dy):
#     print('Mouse scroll (x=%.1f, y=%.1f, dx=%.1f, dy=%.1f)' % (x, y, dx, dy))


def run():
    app.run()
