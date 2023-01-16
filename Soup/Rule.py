class Rule:
    def __init__(self,name,guard,effect):
        self.name = name
        self.guard = guard
        self.effect = effect

    def execute(self,config):
        return [self.effect(config)]


    """ faire 4 instances des cette classe là  alice et bob x2 """

