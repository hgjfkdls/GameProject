from GameEngine.ECS import *

LINE_COUNT = 0


def draw_line(x1, y1, x2, y2, color=(1, 1, 1, 1)):
    global LINE_COUNT
    LINE_COUNT += 1
    e = Entity('line{}'.format(LINE_COUNT))
    e.draw = DrawComponent(
        vertex=[(x1, y1, 0), (x2, y2, 0)],
        index=[0, 1],
        color=color
    )
    return e
