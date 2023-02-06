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


class Str2Tr(TransitionRelation):

    def __init__(self, str):
        self.str = str

    def roots(self):
        #return la config initale de semanticTR cf. plus haut
        return self.str.initalConf()

    def next(self, source):
        actions = self.str.enabledActions(source)
        res = []
        for action in actions:
            res.extend(self.str.execute(action, source))
        return res

