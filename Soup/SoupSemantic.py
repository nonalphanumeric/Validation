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
        return filter(lambda r: r.guard(source), self.program.rules)

    def execute(self, rule, source):
        t = copy.deepcopy(source)
        rule(t)
        return t


class Str2Tr(TransitionRelation):
    iC = [False, False]
    program = SoupProgram(iC)
    s = SoupSemantic(program)
    roots = s.initialConf()
    TransitionRelation.next(roots)


def soup_predicate_verif(soup_program, predicate):
    semantic = SoupSemantic(soup_program)
    transition_relation = Str2Tr(semantic)
    predicate(transition_relation, predicate)
