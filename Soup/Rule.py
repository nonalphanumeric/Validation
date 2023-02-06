class Rule:
    def __init__(self,name,guard,effect):
        self.name = name
        self.guard = guard
        self.effect = effect

    def __str__(self):
        return self.name

    def execute(self,config):
        return [self.effect(config)]



