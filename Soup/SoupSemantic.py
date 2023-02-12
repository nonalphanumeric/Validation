import copy
from abc import ABC

from Misc.transitionRelation import TransitionRelation
from SemanticTransitionRelation import SemanticTransitionRelation
from Soup.SoupProgram import SoupProgram


class SoupSemantic(SemanticTransitionRelation, ABC):
    def __init__(self, program):
        self.program = program

    def initialConf(self):
        return [self.program.ini]

    def enabledActions(self, source):
        return list(filter(lambda r: r.guard(source), self.program.rules))

    def execute(self, rule, source):
        t = copy.deepcopy(source)
        rule.execute(t)  # t : un config cf class Rule
        return [t]




