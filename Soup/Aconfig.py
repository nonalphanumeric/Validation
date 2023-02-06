import copy


class Aconfig:

    def __init__(self):
        pass

    def copy(self):
        return copy.deepcopy(self)


class Config1(Aconfig):
    def __init__(self, x):
        self.x = x

    def copy(self):
        return copy.deepcopy(self)
