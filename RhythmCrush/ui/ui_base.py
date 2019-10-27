from ..interface import IUpdatableObject, IDrawableObject


class BaseUIObject(IUpdatableObject, IDrawableObject):
    def __init__(self, x, y):
        self.position = (x, y)

    def update(self, delta_time):
        pass

    def draw(self):
        raise NotImplementedError()