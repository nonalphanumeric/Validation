from SoupProgram import SoupProgram


class SoupSemantic:
    def __init__(self, program):
        self.program = program

    def initalConf(self):
        return [self.program.ini]

    def enabledActions(self, source):
        return filter(lambda r: r.guard(source), self.program.rules)

    def execute(self, action, source):
        t = source.copy
        return action.execute(t)
