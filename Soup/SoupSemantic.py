from abc import ABC

from Soup.SemanticTransitionRelation import SemanticTransitionRelation
from SoupProgram import SoupProgram


class SoupSemantic(SemanticTransitionRelation, ABC):
    def __init__(self, program):
        self.program = program

    def initalConf(self):
        return [self.program.ini]

    def enabledActions(self, source):
        return filter(lambda r: r.guard(source), self.program.rules)

    def execute(self, rule, source):
        t = source.copy
        return rule.action(t)
